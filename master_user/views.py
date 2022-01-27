# python
from datetime import datetime
import numpy as np

# django
from django.shortcuts import render, redirect, HttpResponse
from django.utils import timezone
from django.contrib import messages
from django.http import JsonResponse
from django.forms.models import model_to_dict

# in app
from .models import WordleAnswers, WordleDayRanks, WordleRanks
from member.models import WordleUser


# Create your views here.
# 화면 첫 진입 시에 사용할 view
def main(request):
    try:
        user_id = request.session["user_id"]
        user = WordleUser.objects.get(user_id=user_id)
        if user.role == 0:  # 일반 유저이면 돌아가도록
            messages.add_message(request, messages.ERROR, "권한이 없습니다.")
            return redirect("member:index_test")
    except:
        return render(
            request, "index/aidle_main.html", {"login_status": "로그인 후 입력해주세요."}
        )

    try:
        a = WordleAnswers.objects.get(date=timezone.now())
        data = a
    except:
        data = ""

    return render(request, "master_user/main.html", {"data": data, "condata": ""})
    # try:
    #     condata = wordle_ranks.objects.filter(date=datetime.now()).select_related('user').order_by('user_rank')
    # except:
    #     condata = ''


# 상위 10명 가져와서 저장하는 view
# day_rank에서 10개 추출 -> rank에 10개 입력 -> day_rank 비우기
def get_top(request):
    # wordle_dayRanks(count=5, user_id=2, create_at=timezone.now()).save()
    # 제출한 시간이 최신 순서대로, 시간이 같다면 카운트가 적은 순서대로 탑 10
    a = WordleDayRanks.objects.all().order_by("count", "recorded_at")[:10]

    # 10개밖에 안되니까 반복문 돌려서 필요한 정보 wordl_ranks에 입력
    for n, i in enumerate(a):
        WordleRanks(user_rank=n + 1, date=i.create_at, user_id=i.user_id).save()

    # dayRanks 의 전체 데이터 삭제
    WordleDayRanks.objects.all().delete()
    return redirect("/master/main")


def get_todayRanker(request):
    try:
        a = (
            WordleRanks.objects.filter(date=datetime.now())
            .select_related("user")
            .order_by("user_rank")
        )
        data = []
        for c in a:
            options = dict()
            options["user_rank"] = c.user_rank
            options["user_name"] = c.user.user_name
            data.append(options)
    except:
        data = "no rank yet"

    return JsonResponse(data, safe=False)


# 오늘자 정답 입력시 동작할 view
def input_answer(request):
    a = request.GET.get("answer")
    try:
        m = WordleAnswers(answer=a)
        m.date = timezone.now()
        m.save()
        return redirect("/master/main")
    except:
        answer = "등록에 실패했습니다."

    return render(request, "master_user/main.html", {"answer": answer})


# 문제 수정 view
def edit_answer(request):
    a = request.GET.get("answer")
    if a:
        w = WordleAnswers.objects.get(date=timezone.now())
        w.answer = a
        w.save()
        return redirect("/master/main")

    return render(request, "master_user/edit.html")


# 문제 삭제 view
def delete_answer(request):
    WordleAnswers.objects.get(date=timezone.now()).delete()

    return redirect("/master/main")


# 더미 데이터 생성
# 나중에 필히 지울것!!!
def dummy(request):
    WordleDayRanks(count=5, user_id=1, recorded_at=timezone.now()).save()
    WordleDayRanks(count=2, user_id=1, recorded_at=timezone.now()).save()
    WordleDayRanks(count=6, user_id=1, recorded_at=timezone.now()).save()
    WordleDayRanks(count=4, user_id=1, recorded_at=timezone.now()).save()
    WordleDayRanks(count=1, user_id=1, recorded_at=timezone.now()).save()
    WordleDayRanks(count=3, user_id=1, recorded_at=timezone.now()).save()

    return HttpResponse("<p>성공</p>")


def class_avg(request):
    # load user's class
    classes = [user_class[1] for user_class in WordleUser.CLASS_CHOICES]
    user_cnt = np.zeros(10)
    class_values = [
        {"class": "", "count": 0, "record": np.array([0, 0, 0, 0])} for i in range(10)
    ]

    # find user class, count, record
    rank_user = WordleDayRanks.objects.select_related("user")
    user_classes = np.array(rank_user.values("user__user_class"))
    user_counts = np.array(rank_user.values("count"))
    user_records = np.array(rank_user.values("recorded_at"))

    # add user values
    for i in range(len(user_classes)):
        class_idx = classes.index(user_classes[i]["user__user_class"])
        class_values[class_idx]["count"] += user_counts[i]["count"]
        class_values[class_idx]["record"] += [
            user_records[i]["recorded_at"].hour,
            user_records[i]["recorded_at"].minute,
            user_records[i]["recorded_at"].second,
            user_records[i]["recorded_at"].microsecond,
        ]
        user_cnt[class_idx] += 1

    for idx in range(len(classes)):
        class_values[idx]["class"] = classes[idx]
        class_values[idx]["count"] = class_values[idx]["count"] / user_cnt[idx]
        class_values[idx]["record"] = (
            class_values[idx]["record"] / user_cnt[idx]
        ).astype(int)
        if np.isnan(class_values[idx]["count"]):
            class_values[idx]["count"] = 0
            class_values[idx]["record"] = [0, 0, 0, 0]

    # change notation
    np.set_printoptions(precision=6, suppress=True)

    return render(
        request,
        "index/aidle_main.html",
        {
            "class_values": class_values,
        },
    )
