import os
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'scraper_rss.settings')

app = Celery('scraper_rss')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
