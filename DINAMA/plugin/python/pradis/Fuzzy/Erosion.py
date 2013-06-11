# -*- coding: iso-8859-1 -*-
#
# Copyright (C) 2009  Rene Liebscher
#
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU Lesser General Public License as published by the Free 
# Software Foundation; either version 3 of the License, or (at your option) any
# later version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT 
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more details.
# 
# You should have received a copy of the GNU Lesser General Public License along with 
# this program; if not, see <http://www.gnu.org/licenses/>. 
#
"""Operator class which takes value of input operator and calculates complement of it."""
__revision__ = "$Id: Not.py,v 1.13 2009/10/07 21:08:14 rliebscher Exp $"

from fuzzy.operator.Operator import Operator

from fuzzy.norm.Norm import NormException
from fuzzy.norm.ParametricNorm import ParametricNorm
from fuzzy.utils import inf_p

class ErosionNorm(ParametricNorm):

	_range = [  (0.,inf_p) ]

	def __init__(self,ps=0.5):
		ParametricNorm.__init__(self,ParametricNorm.T_NORM,ps)

	def __call__(self,*args):
#		if len(args) != 2:
#			raise NormException("%s is supported only for 2 parameters" % self.__class__.__name__ )
		ps = self.p
		x = float(args[0])
#		y = float(args[1])
		return pow(x,ps)

class Erosion(Operator):
	"""Take value of input operator and calculate complement of it.
	   
	   @ivar input: input which result is to complement.
	   @type input: L{fuzzy.operator.Operator.Operator}
	""" 

	def __init__(self, input, ps):
		"""Constructor.
		
		@param input: input which result is to complement.
		@type input: L{fuzzy.operator.Operator.Operator}
		"""
		super(Erosion, self).__init__()
		self.inputs = [input, None]
		self.p = ps 
		self.operatorNorm = ErosionNorm (ps)

	def __call__(self):
		"""Get input value and return 1.0-value."""
		return pow (self.inputs[0](),self.p)
