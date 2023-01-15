# --------------------------------------------------------------
# Python imports
# --------------------------------------------------------------
import os
from datetime import timedelta

# --------------------------------------------------------------
# 3rd party imports
# --------------------------------------------------------------
from celery import Celery

 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'agi.conf.dev')
app = Celery('agi')
app.config_from_object('django.conf:settings', namespace='CELERY')
 
app.conf.timezone = 'Europe/London'

# app.conf.beat_schedule = {
#     "process_coordinates": {
#         "task": "core.tasks.process_coordinates",
#         "schedule": timedelta(minutes=5),
#     },
# }
 
app.autodiscover_tasks()
