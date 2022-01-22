from django.urls import include, path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("post/", include("cal.post.urls")),
]
