from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = "member"

urlpatterns = [
    path("index_test/", views.index_test, name="index_test"),
    path("login/", views.login_custom, name="login"),
    path("logout/", views.logout_custom, name="logout"),
    path("signup/", views.signup_custom, name="signup"),
]
