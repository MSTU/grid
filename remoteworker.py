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
from multigrid.solvers.holder import get_solver

celery = Celery('remoteworker')
celery.config_from_object(config)

@celery.task(name='remoteworker.run_task')
def run_task(task):
	for lc in task.loadcases:
		# TODO May be preexecute must be static method?
		solver = get_solver(lc.solver)
		solver.preexecute(lc)
	return localworker.run_task(task)