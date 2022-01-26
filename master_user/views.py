# python
from datetime import datetime

# django
from django.shortcuts import render, redirect, HttpResponse
from django.utils import timezone
from django.contrib import messages

# in app
from .models import WordleAnswers, WordleDayRanks, WordleRanks
from member.models import WordleUser

# Create your views here.
# 화면 첫 진입 시에 사용할 view
def main(request):
    # try:
    #     user_id = request.session["user_id"]
    #     user = WordleUser.objects.get(user_id=user_id)
    #     if user.role == 0:  # 일반 유저이면 돌아가도록
    #         messages.add_message(request, messages.ERROR, "권한이 없습니다.")
    #         return redirect("member:index_test")
    # except:
    #     return render(
    #         request, "index/aidle_main.html", {"login_status": "로그인 후 입력해주세요."}
    #     )

    try:
        a = WordleAnswers.objects.get(date=timezone.now())
        data = a
    except:
        data = ""
    try:
        condata = (
            WordleRanks.objects.filter(date=datetime.now())
            .select_related("user")
            .order_by("user_rank")
        )
    except:
        condata = ""

    return render(request, "master_user/main.html", {"data": data, "condata": condata})


# 상위 10명 가져와서 저장하는 view
# day_rank에서 10개 추출 -> rank에 10개 입력 -> day_rank 비우기
def get_top(request):
    # wordle_dayRanks(count=5, user_id=2, create_at=timezone.now()).save()
    # 제출한 시간이 최신 순서대로, 시간이 같다면 카운트가 적은 순서대로 탑 10
    a = WordleDayRanks.objects.all().order_by("count", "create_at")[:10]

    # 10개밖에 안되니까 반복문 돌려서 필요한 정보 wordl_ranks에 입력
    for n, i in enumerate(a):
        WordleRanks(user_rank=n + 1, date=i.recorded_at, user_id=i.user_id).save()

    # dayRanks 의 전체 데이터 삭제
    WordleDayRanks.objects.all().delete()
    return redirect("/master/main")


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
    WordleDayRanks(count=5, user_id=1, create_at=timezone.now()).save()
    WordleDayRanks(count=2, user_id=1, create_at=timezone.now()).save()
    WordleDayRanks(count=6, user_id=1, create_at=timezone.now()).save()
    WordleDayRanks(count=4, user_id=1, create_at=timezone.now()).save()
    WordleDayRanks(count=1, user_id=1, create_at=timezone.now()).save()
    WordleDayRanks(count=3, user_id=1, create_at=timezone.now()).save()

    return HttpResponse("<p>성공</p>")
