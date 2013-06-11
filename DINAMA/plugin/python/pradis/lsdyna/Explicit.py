import af
import glb
from misc import *
#from ParameterValues import *

from  lskey import *
from  Launcher import *

# объект импорта файла 

class Explicit (lskey):# (ParameterValues):

	def __init__ (self, nl, pl, desc=misc.default):
		
		self.pl = pl
		add_key (self)
		
#		self.key_name = 'CONTROL_TERMINATION'
		
	def data(self, data):
				
		data += '*CONTROL_TERMINATION\n'+ str(self.pl[0])+',0,0.0,0.0,0.0\n'
		data += '*CONTROL_TIMESTEP\n'+ str(self.pl[1])+',0.90,0,0.0,'+str(self.pl[2])+',0,0,0\n'
		
		return data



