from django.forms import ValidationError

def password_validator(value):
   if len(value) < 8:
       raise ValidationError('비밀번호는 8자 이상이여야 합니다.')
