import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proj.settings')

app = Celery('proj')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

#celery beat tasks

app.conf.beat_schedule = {
    'send-message-every-2-minute': {
        'task':'support.tasks.send_beat_email',
        'schedule': crontab(minute='*/2'),
    },
}