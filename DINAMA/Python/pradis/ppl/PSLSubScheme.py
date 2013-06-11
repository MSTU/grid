import af
import glb
#from OutValue import *
import misc
from SubScheme import *
from Data import *
from SubData import *

class PSLSubScheme:

	def __init__ (self, name, nl, pl, desc= misc.default):
		parlist=[]
		for i in pl:
			pname = i[0]
			pval  = i[1]
			P1 = Data("_psl_"+name+"_"+desc+"_"+pname, pval)
			R1 = SubData(pname, P1)
			parlist.append(R1);
		SubScheme (name, nl, parlist, desc = desc)

	def I (self, n):
		ov = OutValue()
		ov.type = 4
		ov.number = n
		ov.model = self
		return ov

	def W (self, n):
		ov = OutValue()
		ov.type = 7
		ov.number = n
		ov.model = self
		return ov

	def S (self, n):
		ov = OutValue()
		ov.type = 8
		ov.number = n
		ov.model = self
		return ov

