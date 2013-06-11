import af
import glb
from misc import *
from ParameterValues import *

class Pipe (ParameterValues):

	def __init__ (self, nl, pl, desc= misc.default):
		
		self.values = [5, pl]
		
	def Values(self):
		return self.values		
			



