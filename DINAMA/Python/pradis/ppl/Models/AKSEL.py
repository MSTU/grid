from Model import *
from structs import *

class AKSEL (Model):
	def __init__ (self, nl, pl):

		pl = misc.Expand (pl)

		if nl.__class__ != list and nl.__class__ != tuple or pl.__class__ != list and pl.__class__ != tuple:
			ErrPrnMdl (2005, "AKSEL")
			raise af.LVPS_TException ("")
			
		if len (nl) != 2:
			ErrPrnMdl (2007, "AKSEL", 2, len (nl))
			raise af.LVPS_TException ("")

		if len (pl) != 3:
			ErrPrnMdl (2008, "AKSEL", 3, len (pl))
			raise af.LVPS_TException ("")

		if nl[0].__class__ != DOF and nl[0].__class__ != DOF1:
			ErrPrnMdl (2006, "AKSEL", 1, "dof1")
			raise af.LVPS_TException ("")
			
		if nl[1].__class__ != DOF and nl[1].__class__ != DOF1:
			ErrPrnMdl (2006, "AKSEL", 2, "dof1")
			raise af.LVPS_TException ("")
			
		if pl[0].__class__ != int and pl[0].__class__ != long and pl[0].__class__ != float:
			ErrPrnMdl (2004, "AKSEL", 1, "float")
			raise af.LVPS_TException ("")
			
		if pl[1].__class__ != int and pl[1].__class__ != long and pl[1].__class__ != float:
			ErrPrnMdl (2004, "AKSEL", 2, "float")
			raise af.LVPS_TException ("")
			
		if pl[2].__class__ != int and pl[2].__class__ != long and pl[2].__class__ != float:
			ErrPrnMdl (2004, "AKSEL", 3, "float")
			raise af.LVPS_TException ("")
			
		self.this = Model ("mechanics.AKSEL", nl, pl)
