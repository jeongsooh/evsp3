from django import forms
from .models import User

class LoginForm(forms.Form):
  userid = forms.CharField(
    error_messages={
      'required': '사용자 아이디를 입력하세요.'
    },
    max_length=64, label='사용자 아이디'
  )
  password = forms.CharField(
    error_messages={
      'required': '비밀번호를 입력하세요.'
    },
    widget=forms.PasswordInput, label='비밀번호'
  )