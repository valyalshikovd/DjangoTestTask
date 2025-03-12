import os
from celery import Celery


#os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'testProject.settings')

import multiprocessing

from core import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
multiprocessing.set_start_method("spawn", force=True)

app = Celery(
    'testProject',
    include=['userapp.smtp_client_service']
)

app.conf.broker_url = settings.CACHES['default']['LOCATION']
app.conf.result_backend = settings.CACHES['default']['LOCATION']
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()