from django.urls import path
from . import views

app_name = "game"

urlpatterns = [
    path("start", views.start),
    path("main/", views.maintest),
]
