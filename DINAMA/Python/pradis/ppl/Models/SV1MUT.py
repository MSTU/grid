from Model import *
from structs import *

class SV1MUT (Model):
	def __init__ (self, nl, pl):

		pl = misc.Expand (pl)

		mdlname = "mechanics.SV1MUT"
	
		if nl.__class__ != list and nl.__class__ != tuple or pl.__class__ != list and pl.__class__ != tuple:
			ErrPrnMdl (2005, mdlname)
			raise af.LVPS_TException ("")
			
		if len (nl) != 2:
			ErrPrnMdl (2007, mdlname, 2, len (nl))
			raise af.LVPS_TException ("")

		if len (pl) != 1:
			ErrPrnMdl (2008, mdlname, 1, len (pl))
			raise af.LVPS_TException ("")

		for i in range(2):
			if nl[i].__class__ != DOF and nl[i].__class__ != DOF1:
				ErrPrnMdl (2006, mdlname, i+1, "dof1")
				raise af.LVPS_TException ("")
			
		if pl[0].__class__ != Diagram:
			ErrPrnMdl (2004, mdlname, 1, "Diagram")
			raise af.LVPS_TException ("")
			
		self.this = Model (mdlname, nl, [pl[1].GetTable()])
