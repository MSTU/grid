from Model import *
from structs import *

class GVV (Model):
	def __init__ (self, nl, pl):

		pl = misc.Expand (pl)

		mdlname = "hydro.GVV"
	
		if nl.__class__ != list and nl.__class__ != tuple or pl.__class__ != list and pl.__class__ != tuple:
			ErrPrnMdl (2005, mdlname)
			raise af.LVPS_TException ("")
			
		if len (nl) != 5:
			ErrPrnMdl (2007, mdlname, 5, len (nl))
			raise af.LVPS_TException ("")

		if len (pl) != 7:
			ErrPrnMdl (2008, mdlname, 7, len (pl))
			raise af.LVPS_TException ("")

		for i in range(5):
			if nl[i].__class__ != DOF and nl[i].__class__ != DOF1:
				ErrPrnMdl (2006, mdlname, i+1, "dof1")
				raise af.LVPS_TException ("")
			
		for i in range(7):
			if pl[i].__class__ != int and pl[i].__class__ != long and pl[i].__class__ != float:
				ErrPrnMdl (2004, mdlname, i+1, "float")
				raise af.LVPS_TException ("")
			
		self.this = Model (mdlname, nl, pl)
