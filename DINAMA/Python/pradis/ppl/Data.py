import af
import glb
from OutValue import *
import misc
from types import *
import sys


class Data (af.TString):

	def __init__ (self, name, pl):
		sl = glb.sch.GetDataList()
		self.this = af.TString(sl.Add())
		self.SetName(name)
		par = misc.Expand (pl)
		value = ""
		self.value = pl
		
#		print 'data=',par
		
		for i in par:	
#			if value != "":
#				value = value + ", "
#			value +=  str(i)
			if value != "":
				value = value + ", "
			if isinstance(i, Data):
				value +=  i.GetName()
			elif isinstance(i, StringType):
				file_name = sys.argv[0] + ".psl"
				file_name = file_name.replace(".py.",".") 

				af.StringParameter.SetName(file_name)
				code = af.StringParameter.Add (i);
				af.StringParameter.Save()
#				af.StringParameter.Close()
				value += str(code)
				
#				print 'code=',code, '   i=',i
				
			else:
				value +=  str(i)
#				print "data4=", value

#		print len(value)
		self.SetValue((value))
#		print 1111111
#		print self.GetValue()

	def GetOriginalValue(self):
		return self.value
		



