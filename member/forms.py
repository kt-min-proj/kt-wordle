from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import WordleUser  # auth user


class SignUpForm(forms.ModelForm):
    class Meta:
        model = WordleUser
        fields = ["user_id", "user_pw", "user_name", "user_class"]
        labels = {
            "user_id": "ID",
            "user_pw": "PASSWORD",
            "user_name": "NAME",
            "user_class": "CLASS",
        }