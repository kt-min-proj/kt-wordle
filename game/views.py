from django.http import HttpResponse, request
from django.shortcuts import render

def start(request):
    return render(request, "game/game.html")


def maintest(request):
    return render(request, "index/aidle_main.html")
