# -*- coding: cp1251 -*-


#from misc import *
#import Solver
from pradis.Fuzzy.System import System as System
from pradis.Fuzzy.Set import Set as Set
from pradis.Fuzzy.Norm import Norm as Norm
from fuzzy.Adjective import Adjective as adj
#from fuzzy.norm.AlgebraicSum import AlgebraicSum
#from fuzzy.norm import *
#from fuzzy.set.Polygon import Polygon
# объект импорта файла 

# нормы 
#from fuzzy.norm.Max import Max
#from fuzzy.norm.Min import Min
#from fuzzy.norm.BoundedDifference import BoundedDifference
#from fuzzy.norm.DrasticSum import DrasticSum
#from fuzzy.norm.EinsteinSum import EinsteinSum
#from fuzzy.norm.DombiUnion import DombiUnion

#from fuzzy.norm.AlgebraicProduct import AlgebraicProduct
#from fuzzy.norm.AlgebraicSum import AlgebraicSum as AlgebraicSum
#import  fuzzy.norm.AlgebraicSum 

#from  pradis.ppl.constant import *
#import pradis.ppl.constants as constants
import constants as constants

class Adjective :# (ParameterValues):

	def __init__ (self, nl, pl, desc=constants.default):
		
		self.Name = pl[0] 
		self.Set = pl[1]
		self.Values = pl[2]
		self.Norm = pl[3]

		set = Set.choice (self.Set, self.Values)
		norm = Norm.choice (self.Norm)
		
		self.adjective = adj (set, norm)	
		
#		solver = Solver.getSolver()
#		solver.addObject (self)
		
