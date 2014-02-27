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
from solvers.ansys.lsdynasolver import LSDYNASolver

def test_1():
	lc3 = AnsysLoadcase('k_files/bouncing.k', LSDYNASolver.name, "lc3", None, "NCPU=4 ENDTIME=4e-2 O=my_result.out")
	lc4 = AnsysLoadcase('k_files/bouncing.k', LSDYNASolver.name, "lc4_error", None, "O=result.out ENDTIME=ERROR NCPU=1")

	result = map([lc3, lc4], [None])
	result_lc3 = result['lc3']
	result_lc4 = result['lc4_error']

test_1()
