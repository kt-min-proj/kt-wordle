from django.urls import path
from . import views

app_name = "game"

urlpatterns = [
    path("main/", views.mainplay, name="main"),
    path("send/", views.sendinfo, name="send"),
]
