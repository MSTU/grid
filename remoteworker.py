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
import localworker

from ftplib import FTP


celery = Celery('remoteworker', include=[])
celery.config_from_object(config)


def do_file_transfer(loadcase):
	if not os.path.exists(loadcase.name):
		os.makedirs(loadcase.name)
	os.chdir(loadcase.name)

	address = loadcase.transfer_params['host']  # address of host where store files

	ftp = FTP()

	if need_transfer(loadcase.scheme):
		ftp.connect(address, config.FTP_PORT)
		ftp.login(config.FTP_LOGIN, config.FTP_PASSWORD)

		localfile = open(loadcase.scheme, 'w+')
		ftp.retrbinary('RETR ' + loadcase.scheme, localfile.write)

		#TODO need error handling
		localfile.close()
		ftp.quit()

	# change to parent directory
	os.chdir(os.path.abspath(os.path.join(os.getcwd(), os.pardir)))


def need_transfer(filename):
	return not os.path.exists(filename)


@celery.task(name='remoteworker.run_task')
def run_task(task):
	for lc in task.loadcases:
		if lc.is_filetransfer:
			do_file_transfer(lc)
	# set task id
	task.id = run_task.request.id
	return localworker.run_task(task)