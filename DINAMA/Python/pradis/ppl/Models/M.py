from Model import *
from structs import *

class M (Model):
	def __init__ (self, nl, pl):

		pl = misc.Expand (pl)

		mdlname = "mechanics.M"
	
		if nl.__class__ != list and nl.__class__ != tuple or pl.__class__ != list and pl.__class__ != tuple:
			ErrPrnMdl (2005, mdlname)
			raise af.LVPS_TException ("")
			
		if len (nl) != 1:
			ErrPrnMdl (2007, mdlname, 1, len (nl))
			raise af.LVPS_TException ("")

		if len (pl) != 1:
			ErrPrnMdl (2008, mdlname, 1, len (pl))
			raise af.LVPS_TException ("")

		if nl[0].__class__ != DOF and nl[0].__class__ != DOF1:
			ErrPrnMdl (2006, mdlname, 1, "dof1")
			raise af.LVPS_TException ("")
			
		if pl[0].__class__ != int and pl[0].__class__ != long and pl[0].__class__ != float:
			ErrPrnMdl (2004, mdlname, 1, "float")
			raise af.LVPS_TException ("")
			
		self.this = Model (mdlname, nl, pl)
