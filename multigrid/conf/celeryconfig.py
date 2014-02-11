BROKER_URL = 'amqp://guest@localhost//'
CELERY_RESULT_BACKEND = 'amqp'

#CELERY_ROUTES = {'grid.Worker.RunTask': {'queue': 'default'}, 'Worker.TestTask': {'queue': 'default'}}