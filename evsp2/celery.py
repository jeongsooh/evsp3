from __future__ import absolute_import, unicode_literals
import os

from celery import Celery
from django.conf import settings
# from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'evsp2.settings')

app = Celery('evsp2', broker='redis://localhost:6379/1')  
# app = Celery('evsp2')  
app.conf.enable_utc = False

app.conf.update(timezone = 'Asia/Seoul')

app.config_from_object(settings, namespace='CELERY')

# Celery Beat Settings

app.conf.beat_schedule = {
  'cp_status_check': {
    'task': 'clients.tasks.cp_status_check',
    'schedule': 300       # 5min * 60sec
  }
}
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')