# -*- coding: cp1251 -*-

#***************************************************************************
#
#    copyright            : (C) 2013 by Valery Ovchinnikov (LADUGA Ltd.)
#                                       Anton Lapshin
#                                       Anton Kargin
#    email                : laduga@laduga.com
#***************************************************************************
#***************************************************************************
#*                                                                         *
#*   This program is free software; you can redistribute it and/or modify  *
#*   it under the terms of the GNU General Public License as published by  *
#*   the Free Software Foundation; either version 2 of the License, or     *
#*   (at your option) any later version.                                   *
#*                                                                         *
#***************************************************************************/
import os

from celery import Celery
from conf import config
import constants
import localworker
from solvers.holder import get_solver

from ftplib import FTP
from transfer_util import do_file_transfer

from debug import logger


celery = Celery('remoteworker', include=[])
celery.config_from_object(config)


@celery.task(name='remoteworker.run_task')
def run_task(task):
	# save current directory
	cwd = os.getcwd()
	# move to 'loadcases' directory
	directory = os.path.join(cwd, constants.LOADCASES_DIR)
	if not os.path.exists(directory):
		os.makedirs(directory)
	os.chdir(directory)

	try:
		for lc in task.loadcases:
			if lc.is_filetransfer:
				do_file_transfer(lc.transfer_params['host'], lc.name, lc.scheme)
				logger.info('File transfer complete')

			# TODO May be preexecute must be static method?
			solver = get_solver(lc.solver)
			solver.preexecute(lc)
	finally:
		# move to parent directory
		os.chdir(cwd)

	# set task id
	task.id = run_task.request.id
	task = localworker.run_task(task)

	return task

