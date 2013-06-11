import af
import glb
from misc import *
from ParameterValues import *

class GearPar (ParameterValues):

	def __init__ (self, nl, pl, desc= misc.default):
		
		self.values = pl
		
	def Values(self):
		return self.values		
			



