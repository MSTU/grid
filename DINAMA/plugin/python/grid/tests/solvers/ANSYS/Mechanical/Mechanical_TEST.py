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
        ['dat_files/input.dat', '', [], '', 'ANSYS_Mechanical', '%', '%'],
        desc='Mechanical_1')

    mg = ModelGrid.ModelGrid()
    mg.Init()
    mg.SetLoadcases([lc1])

    ma_list = []

    ma1 = ModelAnalysis.ModelAnalysis()
    ma1.options = "-np 4 -m 512"
    ma_list.append(ma1)

    ma2 = ModelAnalysis.ModelAnalysis()
    ma2.options = "-m 256 -np 2"
    ma_list.append(ma2)

    mg.Calculate(ma_list)
    ma_list = mg.WaitAll()

    mg.Init()

test_1()
