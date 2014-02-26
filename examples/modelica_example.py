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
from multigrid import map as multimap

def test_1 ():

	lc1 = ModelicaLoadcase('mos/mydcmotor.mos', desc='lc1')

	input = dict()
	input['resistor1.R'] = [5.0, 2.0]
	input['inductor1.L'] = [0.4, 1.0]
	input['load.J'] = [2.0, 0.5]

	result_list = multimap(lc1, input)['lc1']

	for i in result_list:
		print i
		print '======================================================'

test_1()