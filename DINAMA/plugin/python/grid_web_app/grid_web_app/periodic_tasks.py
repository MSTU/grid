from __future__ import absolute_import

from celery import Celery
import os
from django.conf import settings

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'grid_web_app.settings')

app = Celery('periodic_tasks')
#app.config_from_object('celeryconfig')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object(settings)
#app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

from grid_frontend.models import Job

@app.task
def check_results():
	all_jobs = Job.objects.all()
	for job in all_jobs:
		print job.name