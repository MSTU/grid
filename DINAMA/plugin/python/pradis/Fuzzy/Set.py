# -*- coding: cp1251 -*-
#import multi

from fuzzy.set.Polygon import Polygon
from fuzzy.set.Triangle import Triangle
from fuzzy.set.ZFunction import ZFunction
from fuzzy.set.PiFunction import PiFunction
from fuzzy.set.SFunction import SFunction
from fuzzy.set.Trapez import Trapez
from fuzzy.set.Singleton import Singleton


class Set(object):

	def __init__(self):
		pass
	
	@staticmethod
	def choice (name, values):	
		
		if name == "Polygon":
#			print values
			set = Polygon (values)
		if name == "Triangle":
			set = Triangle (m = values[0], alpha = values[1], beta = values[2], y_max = values[3], y_min = values[4] ) #m=0.0, alpha=1.0, beta=1.0, y_max=1.0, y_min=0.0
		if name == "ZFunction":
			set = ZFunction (a = values[0], delta = values[1]) #a=0.0, delta=1.0
		if name == "PiFunction":
			set = PiFunction (a = values[0], delta = values[1]) #a=0.0, delta=1.0
		if name == "SFunction":
			set = SFunction (a = values[0], delta = values[1])
		if name == "Trapez":
			set = Trapez (*values) #m1 = values[0], m2 = values[1], alpha = values[3], alpha = values[3],beta=values[4])
		if name == "Singleton":
			set = Singleton (*values) #m1 = values[0], m2 = values[1], alpha = values[3], alpha = values[3],beta=values[4])
		
		# TODO: другие типы множеств
		
		return set
