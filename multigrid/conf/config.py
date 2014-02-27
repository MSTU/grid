
BROKER_URL = 'amqp://guest@localhost//'
CELERY_RESULT_BACKEND = 'amqp'

FTP_PORT = 2112
FTP_LOGIN = ''
FTP_PASSWORD = ''


try:
	from local_conf import *
except:
	pass