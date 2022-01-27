from django.urls import path
from . import views

app_name = "master"
urlpatterns = [
    path("main/", views.main),
    path("get_top/", views.get_top),
    path("input_answer/", views.input_answer),
    path("edit-answer/", views.edit_answer),
    path("delete_answer/", views.delete_answer),
    path("get_todayRanker/", views.get_todayRanker),
    path("dummy_dayData/", views.dummy),
    path("class_avg/", views.class_avg),
]
