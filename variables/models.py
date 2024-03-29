from django.db import models

# Create your models here.

class Variables(models.Model):
  variable = models.CharField(max_length=64, blank=True, verbose_name="기준변수")   
  group = models.CharField(max_length=64, blank=True, verbose_name="적용대상")    # group01, group02, group03
  value = models.IntegerField(null=True, verbose_name='설정값')

  def __str__(self):
    return self.variable

  class Meta:
    db_table = 'evsp2_variables'
    verbose_name = '운용변수'
    verbose_name_plural = '운용변수'

class Confkeys(models.Model):
  key = models.CharField(max_length=64, blank=True, verbose_name="키네임")
  readonly = models.CharField(max_length=64, blank=True, verbose_name="권한설정")
  value = models.CharField(max_length=64, blank=True, verbose_name="설정값")

  def __str__(self):
    return self.key

  class Meta:
    db_table = 'evsp2_confkeys'
    verbose_name = '설정값'
    verbose_name_plural = '설정값'
