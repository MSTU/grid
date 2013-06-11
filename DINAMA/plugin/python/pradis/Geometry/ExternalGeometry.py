import af
import glb
from misc import *
from ParameterValues import *

class ExternalGeometry (ParameterValues):

	def __init__ (self, nl, pl, desc= misc.default):
		
		self.values = [12, pl]
		
	def Values(self):
		return self.values		
			



