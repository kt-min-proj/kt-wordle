from django.urls import path

from . import views

urlpatterns = [
    path("", view=views.calendar_view, name="index"),
]
