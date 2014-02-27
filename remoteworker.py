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
from celery import Celery
from conf import config
import localworker

from ftplib import FTP

celery = Celery('remoteworker', include=['task', 'cloudpickle'])
celery.config_from_object(config)

def do_file_transfer(loadcase):
	ftp = FTP()
	ftp.connect(config.IP_ADDRESS, config.FTP_PORT)
	ftp.login(config.FTP_LOGIN, config.FTP_PASSWORD)

	localfile = open(loadcase.scheme)
	ftp.retrbinary('RETR ' + loadcase.scheme, localfile.write)

	#TODO need error handling
	localfile.close()
	ftp.quit()


@celery.task(name='grid.remoteworker.run_task')
def run_task(task):
	for lc in task.loadcases:
		if lc.need_filetransfer:
			do_file_transfer(lc)
	return localworker.run_task(task)