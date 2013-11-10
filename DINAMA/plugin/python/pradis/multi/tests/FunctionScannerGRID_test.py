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
import pradis.multi.Variable as V
import pradis.multi.FunctionScannerGRID as FSG

def test_1 ():

    lc1 = Loadcase.Loadcase ([],
        ['mos/mydcmotor.mos', '', [], '', 'ModelicaDynamic', '%', '%'],
        desc = 'lc1')
    var1 = V.Variable([], ['resistor1.R', 5.0, 1.0, 10.0], desc = 'R')
    var2 = V.Variable([], ['inductor1.L', 0.4, 0.1, 1.0], desc = 'L')
    fsg = FSG.FunctionScanner([],
    [[var1, var2], [4, 4], [lc1]],
    desc = 'FSG')

    fsg.Run()

test_1()
