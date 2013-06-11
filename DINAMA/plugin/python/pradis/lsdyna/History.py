import af
import glb
from misc import *
#from ParameterValues import *

from  lskey import *
from  Launcher import *

# объект импорта файла 

class HISTORY (lskey):# (ParameterValues):

	def __init__ (self, nl, pl, desc=misc.default):
		
		self.pl = pl
		add_key (self)
				
	def data(self, data):
				
		
		data += '*DATABASE_HISTORY_'+ str(self.pl[0])
		if pl[1]=='set':
			data += '_'+ str(self.pl[1])
		data += '\n'
		
		s = str(pl[2][0])
		for i in pl[2][1:] :
			s += ','+str(i)
		data += '\n'
		
		return data



