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
from multigrid.loadcases.ansysloadcase import AnsysLoadcase
from multigrid.modelgrid import ModelGrid
from solvers.ansys.cfxsolver import CFXSolver


def test_1():
	lc1 = AnsysLoadcase('def_files/StaticMixer.def', CFXSolver.name, "lc1", None,
						"-fullname CFX_result -output-summary-option 2")
	lc2 = AnsysLoadcase('def_files/StaticMixer.def', CFXSolver.name, "lc2", None,
						"-fullname CFX_res -v -output-summary-option 0 -save -name CFX_solution")

	mg = ModelGrid()
	mg.reinit()
	mg.set_loadcases([lc1])
	mg.calculate([None])
	mg.clear_loadcases()
	mg.set_loadcases([lc2])
	mg.calculate([None])
	result_list = mg.wait_all()
	mg.reinit()

test_1()
