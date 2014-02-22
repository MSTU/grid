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

def test_1():

    lc1 = Loadcase.Loadcase([],
        ['def_files/StaticMixer.def', 'CFX_result', [], '', 'ANSYS_CFX', '%', '%'],
        desc='CFX_loadcase_1')

    mg = ModelGrid.ModelGrid()
    mg.clear_tasks()
    mg.set_loadcases([lc1])

    ma_list = []

    ma1 = ModelAnalysis.ModelAnalysis()
    ma1.options = "-output-summary-option 2"
    ma_list.append(ma1)

    ma2 = ModelAnalysis.ModelAnalysis()
    ma2.options = "-v -output-summary-option 0 -save -name CFX_solution"
    ma_list.append(ma2)

    mg.calculate(ma_list)
    ma_list = mg.wait_all()

    mg.clear_tasks()

test_1()
