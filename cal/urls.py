from django.urls import include, path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("cal/", views.cal, name="cal"),
    path("post/", include("cal.post.urls")),
]
