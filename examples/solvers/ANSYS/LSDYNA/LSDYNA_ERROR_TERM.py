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

def test_1 ():

    lc1 = Loadcase.Loadcase ([],
        ['k_files/bouncing.k', 'my_result.out', [], '', 'ANSYS_LS-DYNA', '%', '%'],
        desc='loadcase_2(ERROR)')

    mg = ModelGrid.ModelGrid()
    mg.clear_tasks()
    mg.set_loadcases([lc1])

    ma_list = []

    ma1 = ModelAnalysis.ModelAnalysis()
    par1 = {}
    par1['NCPU'] = 4
    par1['ENDTIME'] = "ERROR IS HERE"
    ma1.SetParameters(par1)
    ma_list.append(ma1)

    ma2 = ModelAnalysis.ModelAnalysis()
    par2 = {}
    par2['ENDTIME'] = 8e-2
    par2['NCPU'] = 1
    ma2.SetParameters(par2)
    ma_list.append(ma2)

    mg.calculate(ma_list)
    ma_list = mg.wait_all()

    mg.clear_tasks()

test_1()
