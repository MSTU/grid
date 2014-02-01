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

def func_1 (ma):
	ma.Status = 0
	return ma.GetParameter ('x')**2

def f1 (ma):
	ma.Status = 0
	x = ma.GetParameter ('x')
	y = ma.GetParameter ('y')
	return (x-2)**2 + (y-1)**2

def f2(ma):
	ma.Status = 0
	x = ma.GetParameter ('x')
	y = ma.GetParameter ('y')
	return (x-5)**2 + (y-5)**2