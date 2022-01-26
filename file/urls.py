from django.urls import path
from . import views

app_name = "file"
urlpatterns = [
    path("upload/", views.upload),
    path("download/", views.download, name='download')
]
