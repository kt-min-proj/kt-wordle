from select import select
from django import forms
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User     # auth user
from .models import User     # auth user

class SignUpForm(forms.ModelForm):
    # password1 = forms.CharField()
    class Meta:
        model = User
        fields = ['user_id', 'user_pw', 'user_name', 'user_class']
        labels = {
            'user_id': 'ID',
            'user_pw': 'PASSWORD',
            'user_name': 'NAME',
            'user_class': 'CLASS'
        }
    
    def clean(self):
        cleaned_data = super().clean()
        user_id = cleaned_data.get('user_id', '')
        user_pw = cleaned_data.get('user_pw', '')
        user_name = cleaned_data.get('user_name', '')
        user_class = cleaned_data.get('user_class', '')

        if 8 > len(user_pw):
            return self.add_error('user_pw', '비밀번호는 8자 이상이여야 합니다.')
        else:
            self.user_id = user_id
            self.user_pw = user_pw
            self.user_name = user_name
            self.user_class = user_class

        return super().clean()