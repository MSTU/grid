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

from multigrid import map as multimap
from multigrid.solvers.python import PythonLoadcase

import matplotlib.pyplot as plt


def func_1(pair):
	x = pair[0]
	y = pair[1]
	return (x - 2) ** 2 + (y - 1) ** 2


def func_2(pair):
	x = pair[0]
	y = pair[1]
	return (x - 5) ** 2 + (y - 5) ** 2


def test_1():

	lc1 = PythonLoadcase(func_1)
	lc2 = PythonLoadcase(func_2)

	input_list = [(x, y) for y in xrange(6) for x in xrange(6)]

	result = multimap([lc1, lc2], input_list)
	f1 = result[func_1.__name__]
	f2 = result[func_2.__name__]

	plt.scatter(f1, f2)
	plt.show()

test_1()

