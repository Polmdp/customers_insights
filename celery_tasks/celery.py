

from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab

# Establece el entorno predeterminado de Django para que Celery lo use
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Customers_Insights.settings')

app = Celery('Customers_Insights')

# Usa la configuración de la base de datos de Django
app.config_from_object('django.conf:settings', namespace='CELERY')

# Descubre automáticamente las tareas en tus aplicaciones de Django
app.autodiscover_tasks()

# Programa para Celery Beat
app.conf.beat_schedule = {
    'send-weekly-email': {
        'task': 'celery_tasks.tasks.send_weekly_email',
        'schedule': crontab(hour=8, minute=0, day_of_week=1),
    },
}
