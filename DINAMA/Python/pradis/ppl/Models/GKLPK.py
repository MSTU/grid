from Model import *
from structs import *

class GKLPK (Model):
	def __init__ (self, nl, pl):

		pl = misc.Expand (pl)

		mdlname = "hydro.GKLPK"
	
		if nl.__class__ != list and nl.__class__ != tuple or pl.__class__ != list and pl.__class__ != tuple:
			ErrPrnMdl (2005, mdlname)
			raise af.LVPS_TException ("")
			
		if len (nl) != 4:
			ErrPrnMdl (2007, mdlname, 4, len (nl))
			raise af.LVPS_TException ("")

		if len (pl) != 8:
			ErrPrnMdl (2008, mdlname, 8, len (pl))
			raise af.LVPS_TException ("")

		for i in range(4):
			if nl[i].__class__ != DOF and nl[i].__class__ != DOF1:
				ErrPrnMdl (2006, mdlname, i+1, "dof1")
				raise af.LVPS_TException ("")
			
		for i in range(8):
			if pl[i].__class__ != int and pl[i].__class__ != long and pl[i].__class__ != float:
				ErrPrnMdl (2004, mdlname, i+1, "float")
				raise af.LVPS_TException ("")
			
		self.this = Model (mdlname, nl, pl)
