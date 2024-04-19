# Generated by Django 5.0.3 on 2024-04-19 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cpinfo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cpinfo',
            name='cpstatus',
            field=models.CharField(choices=[('정상', 'Accepted'), ('정지', 'Rejected'), ('가동대기', 'Pending')], default='정상', max_length=64),
        ),
    ]