import af
import glb
from OutValue import *
import misc

class SubScheme:
# (af.Scheme):

	def __init__ (self, name, nl, pl, desc=misc.default):
		return
		sl = glb.sch.GetModelList()
		self.this = af.Scheme (sl.Add())
		if desc != misc.default:
			self.SetDescription(desc)
		self.SetObjectName (name)
		misc.AddParameters (self, pl)
#		prmlist = af.TList (self.SetParameterList())
#		par = misc.Expand (pl)
#		for i in par:
#			prm = af.TReal (prmlist.Add())
#			prm.SetValue (float(i))
		ndlist = af.TList (self.SetNodeList())
		for i in nl:
			ndlist.Add(i)

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

