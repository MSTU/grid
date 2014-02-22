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

from multigrid.solvers.modelicasolver import ModelicaLoadcase
from multigrid.multigrid import  MultiGrid

def test_1 ():

	lc1 = ModelicaLoadcase('mos/mydcmotor.mos', desc='lc1')

	mg = MultiGrid()
	mg.clear_tasks()
	mg.set_loadcases([lc1])

	input_list = []

	par = dict()
	par['resistor1.R'] = 5.0
	par['inductor1.L'] = 0.4
	par['load.J'] = 2.0
	input_list.append(par)

	par = dict()
	par['resistor1.R'] = 2.0
	par['inductor1.L'] = 1.0
	par['load.J'] = 0.5
	input_list.append(par)

	mg.calculate(input_list)
	result_list = mg.wait_all()

	for i in result_list:
		print i
		print '======================================================'

	mg.clear_tasks()

test_1()
