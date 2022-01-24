from django.http import HttpResponse
from django.shortcuts import render


def start(request):
    answer = "12345679"  # 테스트용 정답
    return render(request, "game/game.html", {"answer": answer})

def maintest(request) :
    return render(request,"index/aidle_main.html")
