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
from multigrid.solvers.python import PythonLoadcase
from multigrid import map as multimap

def func_2(x):
	return x**2


def func_1(x):
	return func_2(x)


def test_1():
	lc = PythonLoadcase(func_1)
	input_list = range(10)
	result_list = multimap(lc, input_list)[func_1.__name__]

	for (param, result) in zip(input_list, result_list):
		print "x = " + str(param) + " y = " + str(result)


test_1()
