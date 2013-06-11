# -*- coding: cp1251 -*-

from fuzzy.fuzzify.Plain import Plain
from fuzzy.fuzzify.Dict import Dict as fDict

from fuzzy.defuzzify.COG import COG
from fuzzy.defuzzify.COGS import COGS
from fuzzy.defuzzify.Dict import Dict 
from fuzzy.defuzzify.LM import LM as LeftLocalMaximum
from fuzzy.defuzzify.RM import RM as RightLocalMaximum
from fuzzy.defuzzify.MaxLeft import MaxLeft as LeftGlobalMaximum
from fuzzy.defuzzify.MaxRight import MaxRight as RightGlobalMaximum

from fuzzy.norm.AlgebraicProduct import AlgebraicProduct
from fuzzy.norm.AlgebraicSum import AlgebraicSum

class Fuzzify(object):
	@staticmethod
	def choice (name, values = None):	
		fuzzify = dict()
		fuzzify ['Plain'] = Plain()
		fuzzify ['Dict'] = fDict()
		

		
		return fuzzify [name]
		


		
		
class deFuzzify(object):
	@staticmethod
	def choice (name, values = None):	
		defuzzify = dict()
		INF = AlgebraicProduct()
		ACC = AlgebraicSum()
		COM = AlgebraicSum()
		CER = AlgebraicProduct()
    		
		defuzzify ['COG'] = COG(INF=INF,ACC=ACC,failsafe = 0.)
		defuzzify ['COGS'] = COGS(INF=INF,ACC=ACC,failsafe = 0.)
		defuzzify ['Dict'] = Dict()
		defuzzify ['LeftLocalMaximum'] = LeftLocalMaximum()
		defuzzify ['RightLocalMaximum'] = RightLocalMaximum()
		defuzzify ['LeftGlobalMaximum'] = LeftGlobalMaximum()
		defuzzify ['RightGlobalMaximum'] = RightGlobalMaximum()
		
		# TODO: другие типы множеств
		
		return defuzzify [name]
