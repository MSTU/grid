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
from multigrid.loadcases.pythonloadcase import PythonLoadcase
import multigrid.modelgrid as ModelGrid

def func_2(x):
	return x**2


def func_1(input_params):
	return func_2(input_params['x'])


def test_1():
	lc = PythonLoadcase(func_1)

	mg = ModelGrid.ModelGrid()
	mg.reinit()
	mg.set_loadcases([lc])

	input_list = []
	for i in xrange(20):
		par = dict()
		par['x'] = i
		input_list.append(par)
	mg.calculate(input_list)

	result_list = mg.wait_all()

	for (param, result) in zip(input_list, result_list):
		print "x = " + str(param['x']) + " y = " + str(result[lc.name])
	mg.reinit()

test_1()