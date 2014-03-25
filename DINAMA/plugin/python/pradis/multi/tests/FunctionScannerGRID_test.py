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

from pradis.multi.Variable import Variable
from pradis.multi.FunctionScannerGRID import FunctionScanner
from solvers.modelicasolver import ModelicaLoadcase

def test_1():

	lc1 = ModelicaLoadcase('mos/mydcmotor.mo', desc='lc1',
						   solver_params={'startTime': 0.0, 'stopTime': 10.0, 'numberOfIntervals': 10})
	var1 = Variable([], ['resistor1.R', 5.0, 1.0, 10.0], desc='R')
	var2 = Variable([], ['inductor1.L', 0.4, 0.1, 1.0], desc='L')
	fsg = FunctionScanner([],
	[[var1, var2], [4, 4], [lc1]],
	desc = 'FSG')

	fsg.run()

test_1()
