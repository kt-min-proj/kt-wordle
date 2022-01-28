# python
import numpy as np
from datetime import timezone

# django
from django.utils import timezone
from django.http import HttpResponse, JsonResponse, request
from django.shortcuts import redirect, render

# in app
from master_user.models import WordleAnswers, WordleDayRanks
from member.models import WordleUser

# wordle_answer에서 정답받아보내기
def mainplay(request):
    n = WordleAnswers.objects.get(date=timezone.now())
    data = n
    return render(
        request,
        "index/aidle_main.html",
        {
            "data": data,
            "class_values": class_avg(request),
        },
    )


# 맞춘사람 wordle_dayRank저장 (시간, userid, 횟수)
def sendinfo(request):
    if request.method == "POST":
        recorded_at = request.POST.get("recorded_at")
        user = request.POST.get("user")
        count = request.POST.get("count")

        record = WordleDayRanks(
            recorded_at=timezone.now(), user_id=int(user), count=int(count)
        )
        record.save()
        return render(request, "index/aidle_corr.html")


# class average (class name, count, record)
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

    # average user values
    for idx in range(len(classes)):
        class_values[idx]["class"] = classes[idx]
        class_values[idx]["count"] = round(class_values[idx]["count"] / user_cnt[idx], 1)
        class_values[idx]["record"] = (
            class_values[idx]["record"] / user_cnt[idx]
        ).astype(int)
        if np.isnan(class_values[idx]["count"]):
            class_values[idx]["count"] = 0
            class_values[idx]["record"] = [0, 0, 0, 0]

    # change notation
    np.set_printoptions(precision=6, suppress=True)

    return class_values
