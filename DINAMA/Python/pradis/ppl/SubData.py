import af
import glb
from OutValue import *
import misc
from Data import *

class SubData (af.TString):

	def __init__ (self, name, pl):
		glb.sch.SetParameterList()
		sl = glb.sch.GetParameterList()
		self.this = af.TString(sl.Add())
		self.SetName(name)
#		par = misc.Expand (pl)
		value = ""
#		for i in par:	
#			if value != "":
#				value = value + ", "
#			if isinstance(i, Data):
#				value +=  i.GetName()
#			else:
#				value +=  str(i)

		if isinstance(pl, Data):
			value +=  pl.GetName()
		else:
			vardat = Data (name+"_value", pl)
			value +=  vardat.GetName()


#		print value
		self.SetValue((value))
#		print self.GetValue()
			



