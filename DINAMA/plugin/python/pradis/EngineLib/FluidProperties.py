import af
import glb
from misc import *
from ParameterValues import *

class FluidProperties (ParameterValues):

	def __init__ (self, nl, pl, desc= misc.default):
		
		self.values = pl
		
	def Values(self):
		return self.values		
			
	def TG(self, par, start):
		return par[start+9]

	def MM(self, par, start):
		return par[start+10]

	def Cp(self, par, start):
		return par[start+11]

	def R(self, par, start):
		return par[start+12]

