import af
import glb
import misc
from OutValue import *

class OVP (af.OutVariable):

	def __init__ (self, prvp, nl, pl, desc=misc.default):
		ovplist = glb.sch.GetOutVariableList()
		self.this = af.OutVariable (ovplist.Add())
		if desc != misc.default:
			self.SetDescription(desc)
		self.SetObjectName (prvp)
		misc.AddParameters (self, pl)
		OVList = af.TList (self.SetOutValueList())
		for i in nl:
			ov = af.OutValue (OVList.Add())
			if i.__class__ != OutValue:
				ov.SetOutValueType (1)
				ov.SetNodeOfValue (i)
			else:
				ov.SetOutValueType (i.type)
				if i.type == 2 or i.type == 3:
					ov.SetNodeOfValue (i.node)
				else:
					ov.SetNumber (i.number)
					ov.SetModelOfValue (i.model)
