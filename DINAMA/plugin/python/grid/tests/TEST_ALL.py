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

# пример работы с grid 

def test_1 ():

#	print grid
	# описание расчетного случая
	lc1 = Loadcase.Loadcase ([],['mos/mydcmotor.mos', '', '', 'ModelicaDynamic'], desc = 'lc1')

	# подготовка объекта решателя 
	mg = ModelGrid.ModelGrid()
	mg.Init()
	mg.SetLoadcases ([lc1])

	# подготовка параметров
	ma_list = []

	ma1 = ModelAnalysis.ModelAnalysis()
	par1 = dict()
	par1['resistor1.R'] = 5.0
	par1['inductor1.L'] = 0.4
	par1['load.J'] = 2.0
	ma1.SetParameters(par1)
	ma_list.append(ma1)	

	ma2 = ModelAnalysis.ModelAnalysis()
	par2 = dict()
	par2['resistor1.R'] = 2.0
	par2['inductor1.L'] = 1.0
	par2['load.J'] = 0.5
	ma2.SetParameters(par2)
	ma_list.append(ma2)
		
	# расчет 
	mg.Calculate (ma_list)
	
	# ожидание выполняения расчета
	ma_list = mg.Wait()

	# обработка результатов
	for i in ma_list:
		print i.GetResults()
		print '======================================================'

	# сброс параметров предыдущего расчета
	mg.Init()

# main ():	

test_1()
