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
from multigrid.conf.ConfigHost import ConfigHost
from conf import celeryconfig

celery = Celery('Worker', include=['Task', 'Loadcase', 'cloudpickle'])
# ����� �� ������������ ���� ������ ������������. �� �� Windows 7 64bit �� �� ��������
celery.config_from_object(celeryconfig)

@celery.task(name='grid.Worker.run_task')
def run_task(task):
	config = ConfigHost()
	for lc in task.loadcases:
		solver = config.solvers[lc.solver]
		solver.init()
		task.result_params[lc.name] = solver.run(lc, task.input_params)
	task.recalc_status()

	print "Parameters = " + str(task.input_params)
	print "Results = " + str(task.result_params)
	return task