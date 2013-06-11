import af
import glb
from misc import *
#from ParameterValues import *

from  lskey import *
from  Launcher import *

# объект импорта файла 

class IncludeFile (lskey):# (ParameterValues):

	def __init__ (self, nl, pl, desc=misc.default):
		
		self.file_name = pl[0] 
		add_key (self)
#		Launcher.add_key (self)
		
			
	def data(self, data):
		data =data+ '\n*INCLUDE\n'+ str(self.file_name)+'\n'
		
		return data
			



