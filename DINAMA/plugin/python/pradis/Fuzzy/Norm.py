# -*- coding: cp1251 -*-
#import multi
#import misc

from fuzzy.norm.Max import Max
from fuzzy.norm.Min import Min
#from fuzzy.norm.BoundedDifference import BoundedDifference
from fuzzy.norm.DrasticSum import DrasticSum
from fuzzy.norm.EinsteinSum import EinsteinSum
from fuzzy.norm.DombiUnion import DombiUnion

from fuzzy.norm.AlgebraicProduct import AlgebraicProduct
from fuzzy.norm.AlgebraicSum import AlgebraicSum

class Norm(object):
	@staticmethod
	def choice (name, values=None):	
		norm = dict()
		norm ['AlgebraicSum'] = AlgebraicSum()
		norm ['Max'] = Max()
		norm ['Min'] = Min()
		norm ['AlgebraicProduct'] = AlgebraicProduct()
		norm ['EinsteinSum'] = EinsteinSum()
		norm ['DombiUnion'] = DombiUnion()
		norm ['DrasticSum'] = DrasticSum()
		# TODO: другие типы множеств
		
		return norm[name]


