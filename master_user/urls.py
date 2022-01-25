from django.urls import path
from . import views

urlpatterns = [
    path("main/", views.main),
    path("get_top/", views.get_top),
    path("input_answer/", views.input_answer),
    path("edit-answer/", views.edit_answer),
    path("dummy_dayData/", views.dummy),
]
