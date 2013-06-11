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
import logging

import grid.Loadcase as Loadcase
import grid.ModelGrid as ModelGrid
import grid.ModelAnalysis as ModelAnalysis
import test_lib as test_lib
import grid.GridLogger as GridLogger

# пример работы с grid 

def test_1():
	logger = GridLogger.GridLogger("test_1")
	# описание расчетного случая
	lc1 = Loadcase.Loadcase([], ['', '', [test_lib.func_1], ['[]'], 'Python', '%', '%', ''], desc = 'lc1')

	# подготовка объекта решателя 
	mg = ModelGrid.ModelGrid()
	mg.Init()
	mg.SetLoadcases([lc1])

	# подготовка параметров
	ma_list = []
	for i in xrange(20):
		ma = ModelAnalysis.ModelAnalysis()
		par = dict()
		par['x'] = i
		ma.SetParameters(par)
		ma_list.append(ma)
	# расчет 
	mg.Calculate(ma_list)
	logger.Log(logging.INFO, "Calculate begin...")

	# ожидание выполняения расчета
	ma_list = mg.Wait()
	logger.Log(logging.INFO, "Calculate end...")
	# обработка результатов
	for i in ma_list:
		if (i.GetStatus() == 0):
		#			monitor.Log("x = " + str(i.getParameter('x')) + " y = " + str(i.getResults()['lc1']))
			print "x = " + str(i.GetParameter('x')) + " y = " + str(i.GetResults()['lc1'])
	# сброс параметров предыдущего расчета
	mg.Init()


# main ():	

test_1()