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

import ModelGrid
import ModelAnalysis
import matplotlib.pyplot as plt


# пример работы с grid
from loadcases import Loadcase


def func_1(ma):
	ma.Status = 0
	x = ma.GetParameter('x')
	y = ma.GetParameter('y')
	return (x - 2) ** 2 + (y - 1) ** 2


def func_2(ma):
	ma.Status = 0
	x = ma.GetParameter('x')
	y = ma.GetParameter('y')
	return (x - 5) ** 2 + (y - 5) ** 2


def test_1():
	# описание расчетного случая
	lc1 = Loadcase.Loadcase([], ['', '', [func_1], ['[]'], 'Python', '%', '%', ''], desc='lc1')
	lc2 = Loadcase.Loadcase([], ['', '', [func_2], ['[]'], 'Python', '%', '%', ''], desc='lc2')

	# подготовка объекта решателя
	mg = ModelGrid.ModelGrid()
	mg.clear_tasks()
	mg.set_loadcases([lc1, lc2])

	# подготовка параметров
	ma_list = []
	for x in range(6):
		for y in range(6):
			ma = ModelAnalysis.ModelAnalysis()
			par = dict()
			par['x'] = x
			par['y'] = y
			ma.SetParameters(par)
			ma_list.append(ma)

	# расчет
	mg.calculate(ma_list)

	# ожидание выполняения расчета
	ma_list = mg.wait_all()
	# обработка результатов
	for i in ma_list:
		if i.get_status() == 0:
			print("x = " + str(i.GetParameter('x')) + " y = " + str(i.GetParameter('y')) + " f1 = " + str(
				i.GetResults()['lc1']) + " f2 = " + str(i.GetResults()['lc2']))
	# сброс параметров предыдущего расчета
	f1 = []
	f2 = []
	for i in ma_list:
		f1.append(i.GetResults()['lc1'][0])
		f2.append(i.GetResults()['lc2'][0])

	#for i in range(len(ma_list)):
	#	plt.plot(f1[i],f2[i],marker='o', color='r')
	plt.scatter(f1, f2)
	plt.show()

	mg.clear_tasks()


# main ():

test_1()

