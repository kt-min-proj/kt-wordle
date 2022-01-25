from select import select
from django import forms
from django.contrib.auth.forms import UserCreationForm

# from django.contrib.auth.models import User     # auth user
from .models import User  # auth user


class SignUpForm(forms.ModelForm):
    # password1 = forms.CharField()
    class Meta:
        model = User
        fields = ["user_id", "user_pw", "user_name", "user_class"]
        labels = {
            "user_id": "ID",
            "user_pw": "PASSWORD",
            "user_name": "NAME",
            "user_class": "CLASS",
        }

    def clean_user_class(self):
        user_class = self.data.get("user_class")
        
        if type(int(user_class)) == type(1):
            return user_class

        try:
            classes = [user_class[1] for user_class in User.CLASS_CHOICES]
            user_class = classes.index(self.data.get("user_class"))
            if user_class:
                return user_class
        except:
            self.add_error("user_class", "올바르게 선택해주세요. 존재하지 않는 반입니다.")
