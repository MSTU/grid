import argparse
import os
import subprocess
import sys
from modelgrid import ModelGrid
from conf.configclient import LOCAL_WORK

__all__ = ['calculate', 'get', 'map', 'reload', 'ready']

_instance = ModelGrid(LOCAL_WORK)

calculate = _instance.calculate
get = _instance.get
map = _instance.map
reload = _instance.reload
ready = _instance.ready
web_get = _instance.web_get
web_get_ids = _instance.web_get_ids
web_get_results_from_job = _instance.web_get_results_from_job

def makeParser():
	"""Create arguments parser."""

	parser = argparse.ArgumentParser(
		description="Starts multigrid",
		prog="multigrid",
		)
	parser.add_argument('--worker', '-w',
						action='store_true',
						help="Launch worker",)
	return parser


def main():
	# Generate a argparse parser and parse the command-line arguments
	parser = makeParser()
	args = parser.parse_args()

	if args.worker:
		subprocess.call(['celery', '-A', 'remoteworker', 'worker', '--concurrency', '1' ])