from django.db import models

# Create your models here.

class Cpinfo(models.Model):
  PUBLIC_STATUS = (('공용', '공용'), ('비공용', '비공용'),)
  CP_STATUS = (('정상', 'Accepted'), ('정지', 'Rejected'), ('가동대기', 'Pending'),)

  cpnumber = models.CharField(max_length=64, verbose_name='충전기번호')
  cpsite = models.CharField(max_length=64, verbose_name='충전소이름')
  partner_id = models.CharField(max_length=128, verbose_name='파트너아이디')
  manager_id = models.CharField(max_length=128, verbose_name='관리자아이디')
  public_use = models.CharField(max_length=64, choices=PUBLIC_STATUS, default= '공용')
  cpstatus = models.CharField(max_length=64, choices=CP_STATUS, default= '정상')
  address = models.TextField(verbose_name='주소')
  cpmodel = models.CharField(max_length=64, verbose_name='충전기모델')
  cpmaker = models.CharField(max_length=64, verbose_name='충전기제조사')
  fwversion = models.CharField(max_length=64, verbose_name='펌웨어버전')
  register_dttm = models.DateTimeField(auto_now_add=True, verbose_name='등록일시')
  last_modified_dttm = models.DateTimeField(auto_now_add=True, verbose_name='최종정보변경일시')

  def __str__(self):
    return self.cpnumber

  class Meta:
    db_table = 'evsp2_cpinfo'
    verbose_name = '충전기'
    verbose_name_plural = '충전기'
