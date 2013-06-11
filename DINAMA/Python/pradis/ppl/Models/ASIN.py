from Model import *
from structs import *

class ASIN (Model):
	def __init__ (self, nl, pl):

		pl = misc.Expand (pl)

		if nl.__class__ != list and nl.__class__ != tuple or pl.__class__ != list and pl.__class__ != tuple:
			ErrPrnMdl (2005, "ASIN")
			raise af.LVPS_TException ("")
			
		if len (nl) != 2:
			ErrPrnMdl (2007, "ASIN", 2, len (nl))
			raise af.LVPS_TException ("")

		if len (pl) != 4:
			ErrPrnMdl (2008, "ASIN", 4, len (pl))
			raise af.LVPS_TException ("")

		if nl[0].__class__ != DOF and nl[0].__class__ != DOF1:
			ErrPrnMdl (2006, "ASIN", 1, "dof1")
			raise af.LVPS_TException ("")
			
		if nl[1].__class__ != DOF and nl[1].__class__ != DOF1:
			ErrPrnMdl (2006, "ASIN", 2, "dof1")
			raise af.LVPS_TException ("")
			
		if pl[0].__class__ != int and pl[0].__class__ != long and pl[0].__class__ != float:
			ErrPrnMdl (2004, "ASIN", 1, "float")
			raise af.LVPS_TException ("")
			
		if pl[1].__class__ != int and pl[1].__class__ != long and pl[1].__class__ != float:
			ErrPrnMdl (2004, "ASIN", 2, "float")
			raise af.LVPS_TException ("")
			
		if pl[2].__class__ != int and pl[2].__class__ != long and pl[2].__class__ != float:
			ErrPrnMdl (2004, "ASIN", 3, "float")
			raise af.LVPS_TException ("")
			
		if pl[3].__class__ != int and pl[3].__class__ != long and pl[3].__class__ != float:
			ErrPrnMdl (2004, "ASIN", 4, "float")
			raise af.LVPS_TException ("")
			
		self.this = Model ("mechanics.ASIN", nl, pl)
