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
from multigrid import map
from solvers.ansys.ansysloadcase import AnsysLoadcase
from solvers.ansys.mechanicalsolver import MechanicalSolver


def test_1():

	lc1 = AnsysLoadcase('dat_files/input.dat', MechanicalSolver.name, "lc1", None, "-np 4 -m 512")
	lc2 = AnsysLoadcase('dat_files/input_error.dat', MechanicalSolver.name, "lc2", None, "-m 256 -np 2")

	result = map([lc1, lc2], [None])
	result_1 = result['lc1']
	result_2 = result['lc2']

test_1()
