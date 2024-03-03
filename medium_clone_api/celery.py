import os

from celery import Celery
from django.conf import settings

# TODO: change this in production
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'medium_clone_api.settings.local')

app = Celery('medium_clone_api')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
