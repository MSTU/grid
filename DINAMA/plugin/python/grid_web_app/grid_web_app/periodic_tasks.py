from __future__ import absolute_import

from celery import Celery
import os
from celery.result import AsyncResult
from django.conf import settings

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'grid_web_app.settings')

app = Celery('periodic_tasks')
#app.config_from_object('celeryconfig')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object(settings)
#app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

# imports from django must be after config Celery
from grid_frontend.models import Job, Task

@app.task
def check_results():
	# Get all unfinished tasks
	unfinished_tasks = Task.objects.filter(is_finished=False)
	# Get results if it's ready
	for task in unfinished_tasks:
		print task.task_id
		async_result = AsyncResult(task.task_id)
		print async_result.ready()
		if async_result.ready():
			task.result = async_result.get().result_params
			task.is_finished = True
			task.save()
			print "Task " + task.task_id + " finished"

	# Check if Job finished
	for job in Job.objects.filter(is_finished=False):
		unfinished_tasks = job.task_set.all()
		# Job can be finished if it had at least on Task
		if unfinished_tasks.exists():
			is_finished = True
		else:
			is_finished = False
		for task in unfinished_tasks:
			if task.is_finished:
				is_finished &= True
			else:
				is_finished &= False

		if is_finished:
			job.is_finished = is_finished
			job.save()
			print "Job " + job.name + " is finished"
	print "finished"