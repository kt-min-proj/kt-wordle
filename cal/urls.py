from django.urls import include, path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("test/", views.cal, name="cal"),
    path("post/", include("cal.post.urls")),
]
