import logging
import sys


def setup_logging(level):
	if level == logging.DEBUG:
		logging.basicConfig(level=level, format="%(asctime)s,%(levelname)-7s  %(message)s", datefmt='%H:%M:%S')
	else:
		logging.basicConfig(level=level, stream=sys.stdout, format="%(asctime)s, %(message)s")
	return logging.getLogger('multigrid')


user_level = 'INFO'

# Set logging level to INFO by default
level = eval('logging.%s' % user_level)
logger = setup_logging(level)
