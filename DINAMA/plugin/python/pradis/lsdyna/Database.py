import af
import glb
from misc import *
#from ParameterValues import *

from  lskey import *
from  Launcher import *

# объект импорта файла 

class DATABASE (lskey):# (ParameterValues):

	def __init__ (self, nl, pl, desc=misc.default):
		
		self.pl = pl
		add_key (self)
		
#		self.key_name = 'CONTROL_TERMINATION'
		
	def data(self, data):
				
		if (pl[0]>0.0):
			data += '*DATABASE_BINARY_D3PLOT\n'+ str(self.pl[0])+'\n'
		if (pl[1]>0.0):
			data += '*DATABASE_BINARY_D3THDT\n'+ str(self.pl[1])+'\n'
		if (pl[2]>0.0):
			data += '*DATABASE_GLSTAT\n'+ str(self.pl[2])+'\n'
		if (pl[3]>0.0):
			data += '*DATABASE_MATSUM\n'+ str(self.pl[3])+'\n'
		if (pl[4]>0.0):
			data += '*DATABASE_NODOUT\n'+ str(self.pl[4])+'\n'
		if (pl[5]>0.0):
			data += '*DATABASE_RWFORC\n'+ str(self.pl[5])+'\n'
"""
			if (pl[6]>0.0):
			data += '*DATABASE_DEFORC\n'+ str(self.pl[4])+'\n'
		if (pl[5]>0.0):
			data += '*DATABASE_ELOUT\n'+ str(self.pl[5])+'\n'
		if (pl[6]>0.0):
			data += '*DATABASE_SLEOUT\n'+ str(self.pl[6])+'\n'
		if (pl[7]>0.0):
			data += '*DATABASE_JNTFORC\n'+ str(self.pl[7])+'\n'
		if (pl[8]>0.0):
			data += '*DATABASE_RBDOUT\n'+ str(self.pl[8])+'\n'
		if (pl[9]>0.0):
			data += '*DATABASE_RCFORC\n'+ str(self.pl[9])+'\n'
"""
		
		return data



