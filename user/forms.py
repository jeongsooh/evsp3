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

  def clean(self):
    cleaned_data = super().clean()
    userid = cleaned_data.get('userid')
    password = cleaned_data.get('password')

    if userid and password:
      try:
        user = User.objects.get(userid=userid)
      except User.DoesNotExist:
        self.add_error('userid', '아이디가 없습니다.')
        return

      if password != user.password:
        self.add_error('password', '비밀번호가 틀렸습니다.')
      else:
        self.user_id = user.id
