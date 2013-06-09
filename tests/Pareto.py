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

import ModelAnalysis
import tests.test_lib as test_lib
import GridLogger
import Loadcase
import ModelGrid
import matplotlib.pyplot as plt


# пример работы с grid

def test_1 ():

	logger = GridLogger.GridLogger("test_1")
	# описание расчетного случая
	lc1 = Loadcase.Loadcase ([],[test_lib.f1, '', '', 'Python'], desc = 'lc1')
	lc2 = Loadcase.Loadcase ([],[test_lib.f2, '', '', 'Python'], desc = 'lc2')

	# подготовка объекта решателя
	mg = ModelGrid.ModelGrid()
	mg.Init()
	mg.SetLoadcases ([lc1,lc2])

	# подготовка параметров
	ma_list = []
	for x in range (6):
		for y in range(6):
			ma = ModelAnalysis.ModelAnalysis ()
			par = dict()
			par['x'] = x
			par['y'] = y
			ma.SetParameters (par)
			ma_list.append (ma)

	# расчет
	mg.Calculate (ma_list)
	logger.Log(GridLogger.INFO, "Calculate begin...")

	# ожидание выполняения расчета
	ma_list = mg.Wait()
	logger.Log(GridLogger.INFO, "Calculate end...")
	# обработка результатов
	for i in ma_list:
		if (i.GetStatus()==0):
			print("x = " + str(i.GetParameter('x')) + " y = "  + str(i.GetParameter('y')) +  " f1 = " +  str(i.GetResults()['lc1'])  +  " f2 = "  + str(i.GetResults()['lc2']))
	# сброс параметров предыдущего расчета
	f1 = []
	f2 = []
	for i in ma_list:
		f1.append(i.GetResults()['lc1'][0])
		f2.append(i.GetResults()['lc2'][0])

	#for i in range(len(ma_list)):
	#	plt.plot(f1[i],f2[i],marker='o', color='r')
	plt.scatter(f1,f2)
	plt.show()

	mg.Init()



# main ():

test_1()

