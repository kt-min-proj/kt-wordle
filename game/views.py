from datetime import timezone
from django.utils import timezone
from django.http import HttpResponse, JsonResponse, request
from django.shortcuts import render


from master_user.models import WordleAnswers, WordleDayRanks
from member.models import WordleUser

# wordle_answer에서 정답받아보내기
def mainplay(request):
    n = WordleAnswers.objects.get(date=timezone.now())
    data = n
    return render(request, "index/aidle_main.html", {"data": data})


# 맞춘사람 wordle_dayRank저장 (시간, userid, 횟수)
def sendinfo(request):
    if request.method == "POST":
        recorded_at = request.POST.get("recorded_at")
        user = request.POST.get("user")
        count = request.POST.get("count")

        record = WordleDayRanks(recorded_at=timezone.now(), user_id=int(user), count=int(count))
        record.save()
    return HttpResponse('성공?')
