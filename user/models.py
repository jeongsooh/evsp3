from django.db import models

# Create your models here.

class User(models.Model):
    userid = models.CharField(max_length=64, verbose_name='회원아이디')
    password = models.CharField(max_length=128, verbose_name='비밀번호')
    name = models.CharField(max_length=64, verbose_name='이름')
    email = models.EmailField(max_length=128, verbose_name='이메일')
    phone = models.CharField(max_length=64, verbose_name='전화번호')
    register_dttm = models.DateTimeField(auto_now_add=True, verbose_name='등록일시')
    last_use_dttm = models.DateTimeField(auto_now_add=True, verbose_name='최근사용일시')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'evsp2_user'
        verbose_name = '회원'
        verbose_name_plural = '회원'