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
import conf.ConfigHost as ConfigHost
import conf.celeryconfig as celeryconfig

celery = Celery('Worker')
celery.config_from_object(celeryconfig)

@celery.task
def RunTask(task):
	config = ConfigHost.ConfigHost()
	for i in task.lc:
		solver = config.solvers[i.Solver]
		solver.Init()
		status = solver.Run(i, task.ma)
		if status < task.GetModelAnalysis().GetStatus():
			task.ma.SetStatus(status)

	print "Parameters = " + str(task.ma.GetParameters())
	print "Results = " + str(task.ma.GetResults())
	return task