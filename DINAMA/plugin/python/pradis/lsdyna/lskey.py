#import af
#import glb
#from misc import *
#from ParameterValues import *

# объект ключа ls-dyna

class lskey:# (ParameterValues):

	def __init__ (self):
		
		self.key_name = ""
		self.pl = []
#		self.nl = []
		Launcher.add_key (self)

	def setKey (self, kn):
		
		self.key_name = kn 
		self.pl = []

		
	def set(self, pl):
		self.pl = pl
#		self.nl = range (pl.length()+1)
		
	def add(self, pl):
		self.pl.appaned(pl)
#		self.nl = range (pl.length()+1)
		
	def add (self, value, name):
		self.pl.append (value)
		
			
	def data(self, d):
		d = d + ('*'+ self.key_name+'\n')
		s = str(self.pl[0])
		for i in self.pl[1:]:
			s=s+', '+ str (i)
		d += s
		
		return d
			



