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
import Loadcase
import ModelGrid
import ModelAnalysis


def func_2(x):
	return x**2


def func_1(ma):
	ma.Status = 0
	return func_2(ma.GetParameter ('x'))


def test_1():
	lc1 = Loadcase.Loadcase([], ['', '', [func_1], ['[]'], 'Python', '%', '%', ''], desc = 'lc1')

	mg = ModelGrid.ModelGrid()
	mg.Init()
	mg.SetLoadcases([lc1])

	ma_list = []
	for i in xrange(20):
		ma = ModelAnalysis.ModelAnalysis()
		par = dict()
		par['x'] = i
		ma.SetParameters(par)
		ma_list.append(ma)
	mg.Calculate(ma_list)

	ma_list = mg.WaitAll()
	for i in ma_list:
		if (i.GetStatus() == 0):
			print "x = " + str(i.GetParameter('x')) + " y = " + str(i.GetResults()['lc1'])
	mg.Init()

test_1()