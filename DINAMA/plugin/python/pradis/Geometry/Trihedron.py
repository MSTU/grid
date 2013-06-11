import af
import glb
from misc import *
from ParameterValues import *

class Trihedron (ParameterValues):

	def __init__ (self, nl, pl, desc= misc.default):
		
		self.values = [1, pl]
		
	def Values(self):
		return self.values		
			



