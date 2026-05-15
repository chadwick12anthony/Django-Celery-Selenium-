import os

from celery import Celery
# from celery. schedules import crontab
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djacese.settings")

app = Celery("djacese")

# Using a string here means the worker don't have to serialize
# the configuration object to child processes.
# - namespace 'CELERY' means all celery-related configuratiofi keys
# should have a CELERY prefix.
app. config_from_object("django.conf:settings", namespace="CELERY")
# Load task modules from all registered Django app configs.

app.autodiscover_tasks()