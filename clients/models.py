from django.db import models

# Create your models here.

class Clients(models.Model):
  cpnumber = models.CharField(max_length=64, blank=True, verbose_name='충전기번호')
  cpstatus = models.CharField(max_length=64, blank=True, verbose_name='충전기상태')
  check_dttm = models.DateTimeField(blank=True, null=True, verbose_name='확인일시')
  channel_name_1 = models.CharField(max_length=64, blank=True, verbose_name='채널1이름')
  channel_status_1 = models.CharField(max_length=64, blank=True, verbose_name='채널1상태')
  connection_id_1 = models.CharField(max_length=256, blank=True, null=True, verbose_name='커넥션1아이디')
  authorized_tag_1 = models.CharField(max_length=64, blank=True, verbose_name='승인된1카드테그')
  channel_name_2 = models.CharField(max_length=64, blank=True, verbose_name='채널2이름')
  channel_status_2 = models.CharField(max_length=64, blank=True, verbose_name='채널2상태')
  connection_id_2 = models.CharField(max_length=256, blank=True, verbose_name='커넥션2아이디')
  authorized_tag_2 = models.CharField(max_length=64, blank=True, verbose_name='승인된2카드테그')

  def __str__(self):
    return self.cpnumber

  class Meta:
    db_table = 'evsp2_clients'
    verbose_name = '충전기채널'
    verbose_name_plural = '충전기채널'
