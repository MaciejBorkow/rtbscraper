from __future__ import absolute_import, unicode_literals

import os

from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webscraper.settings')
app = Celery('webscraper')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.conf.update(worker_concurrency=os.environ.get('CELERY_CONCURRENCY', 20))
app.autodiscover_tasks()
