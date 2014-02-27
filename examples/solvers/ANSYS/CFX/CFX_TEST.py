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
from solvers.ansys.ansysloadcase import AnsysLoadcase
from solvers.ansys.cfxsolver import CFXSolver

from multigrid import calculate
from multigrid import get


def test_1():
	lc1 = AnsysLoadcase('def_files/StaticMixer.def', CFXSolver.name, "lc1", None,
						"-fullname CFX_result -output-summary-option 2")
	lc2 = AnsysLoadcase('def_files/StaticMixer.def', CFXSolver.name, "lc2", None,
						"-fullname CFX_res -v -output-summary-option 0 -save -name CFX_solution")

	lc1_ids = calculate(lc1, [None])
	lc2_ids = calculate(lc2, [None])
	lc1_results = get(lc1_ids)
	lc2_results = get(lc2_ids)

test_1()
