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

import grid.ModelAnalysis as ModelAnalysis
import grid.tests.test_lib as test_lib
import grid.GridLogger as GridLogger
import grid.Loadcase as Loadcase
import grid.ModelGrid as ModelGrid
import matplotlib.pyplot as plt

import constants
import misc
# пример работы с grid

class Pareto:
	def __init__(self, nl, pl, desc = constants.default):

		logger = GridLogger.GridLogger("test_1")
		
		
		
		lc_list = pl[0]    # список расчетных случаев, считаем что их только 2
		var_list = pl[1]   # список переменных, считаем, что их только 2
		count = pl[2]
		
		# описание расчетного случая
		lc1 = lc_list[0].lc
		lc2 = lc_list[1].lc
#		print type(lc1.vl[0])
		# подготовка объекта решателя
		mg = ModelGrid.ModelGrid()
		mg.Init()
		mg.SetLoadcases ([lc1,lc2])

		# подготовка параметров
		ma_list = []
		for x in xrange (count):
			for y in xrange(count):
				ma = ModelAnalysis.ModelAnalysis ()
				par = dict()
				par['x'] = var_list[0].Min + (var_list[0].Max - var_list[0].Min) * float (x) / float(count)
				par['y'] =  var_list[1].Min + (var_list[1].Max - var_list[1].Min) * float (y) / float(count)
				ma.SetParameters (par)
				ma_list.append (ma)

		# расчет
		mg.Calculate (ma_list)
		logger.Log(logging.INFO, "Calculate begin...")

		# ожидание выполняения расчета
		ma_list = mg.Wait()
		logger.Log(logging.INFO, "Calculate end...")
		# обработка результатов
		for i in ma_list:
			if (i.GetStatus()==0):
				print("x = " + str(i.GetParameter('x')) + " y = "  + str(i.GetParameter('y')) +  " f1 = " +  str(i.GetResults()[lc1.Name])  +  " f2 = "  + str(i.GetResults()[lc2.Name]))
		# сброс параметров предыдущего расчета
		f1 = []
		f2 = []
		for i in ma_list:
			f1.append(i.GetResults()[lc1.Name][0])
			f2.append(i.GetResults()[lc2.Name][0])

		#for i in range(len(ma_list)):
		#	plt.plot(f1[i],f2[i],marker='o', color='r')
		plt.scatter(f1,f2)
		plt.show()

		mg.Init()
		misc.SetSolver ("")
#		misc.SetPost(os.getenv("DINSYS")+"\dinama\post\Postprocessor")
		misc.SetPost("")		
#		misc.SetPostFile(self.ma.GetHistoryFile())
		


# main ():

#test_1()

