# Generated by Django 5.0.3 on 2024-03-25 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Charginginfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpnumber', models.CharField(max_length=64, verbose_name='충전기번호')),
                ('userid', models.CharField(max_length=64, verbose_name='회원아이디')),
                ('energy', models.IntegerField(verbose_name='충전량')),
                ('amount', models.IntegerField(verbose_name='충전금액')),
                ('start_dttm', models.DateTimeField(verbose_name='충전시작일시')),
                ('end_dttm', models.DateTimeField(verbose_name='충전완료일시')),
            ],
            options={
                'verbose_name': '충전정보',
                'verbose_name_plural': '충전정보',
                'db_table': 'evsp2_charginginfo',
            },
        ),
    ]
