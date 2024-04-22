#!/bin/bash

cd /home/jeongsooh/projects/evsp

source venv/bin/activate
cd evsp3

# celery execution
celery -A evsp2 worker -l INFO &
celery -A evsp2 beat -l INFO &

python manage.py runserver 0.0.0.0:8000