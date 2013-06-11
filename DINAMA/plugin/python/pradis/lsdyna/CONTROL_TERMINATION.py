import af
import glb
from misc import *
#from ParameterValues import *

from  lskey import *
from  Launcher import *

# объект импорта файла 

class CONTROL_TERMINATION (lskey):# (ParameterValues):

	def __init__ (self, nl, pl, desc=misc.default):
		
		self.pl = pl
		add_key (self)
		self.key_name = 'CONTROL_TERMINATION'
		
	"""	
	def data(self, data):
		
		return lskey.data()
		
		s = pl[0]
		for i in self.pl[1:]:
		
			s=s+', ', str(i)
		
		data += '*CONTROL_TERMINATION\n'+ str(self.pl)+'\n'
		
		return data
	"""		



