# import django
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.http import HttpResponse

# third party app
from argon2 import PasswordHasher

# import app
from .models import User
from .forms import SignUpForm

# Create your views here.


def index_test(request):
    return render(request, "index/aidle_main.html")


def signup_custom(request):
    classes = [
        "수도권1반",
        "수도권2반",
        "수도권3반",
        "수도권4반",
        "수도권5반",
        "강원권1반",
        "충남/충북권1반",
        "대구/경북권1반",
        "전남/전북권1반",
        "부산/경남권1반",
    ]

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)  # integer로 변경해서 저장
            user.user_pw = PasswordHasher().hash(user.user_pw)
            user.save()
            # login
            return redirect("member:login")  # game page
    else:
        form = SignUpForm()

    return render(
        request,
        # 'index/aidle_signup.html',
        "member/signup.html",
        {
            "form": form,
            "classes": classes,
        },
    )


def login_custom(request):
    if request.method == "POST":
        user_id = request.POST.get("user_id")
        user_pw = request.POST.get("user_pw")
        try:
            user = User.objects.get(user_id=user_id)
            password = user.user_pw
            if not PasswordHasher().verify(password, user_pw.encode()):
                return render(
                    request,
                    "member/login.html",
                    {"login_status": "ID 혹은 PASSWORD를 확인해주세요."},
                )
        except User.DoesNotExist as e:
            return render(
                request,
                "member/login.html",
                {"login_status": "ID 혹은 PASSWORD를 확인해주세요."},
            )
        else:
            request.session["user_id"] = user.user_id
            request.session["user_name"] = user.user_name
        return redirect("member:index_test")
    else:
        return render(request, "member/login.html")


def logout_custom(request):
    del request.session["user_id"]  # 개별 삭제
    del request.session["user_name"]  # 개별 삭제
    request.session.flush()  # 전체 삭제
    return redirect("member:login")
