from Model import *
from structs import *

class ATABL (Model):
	def __init__ (self, nl, pl):

		pl = misc.Expand (pl)

		if nl.__class__ != list and nl.__class__ != tuple or pl.__class__ != list and pl.__class__ != tuple:
			ErrPrnMdl (2005, "ATABL")
			raise af.LVPS_TException ("")
			
		if len (nl) != 2:
			ErrPrnMdl (2007, "ATABL", 2, len (nl))
			raise af.LVPS_TException ("")

		if len (pl) != 2:
			ErrPrnMdl (2008, "ATABL", 2, len (pl))
			raise af.LVPS_TException ("")

		if nl[0].__class__ != DOF and nl[0].__class__ != DOF1:
			ErrPrnMdl (2006, "ATABL", 1, "dof1")
			raise af.LVPS_TException ("")
			
		if nl[1].__class__ != DOF and nl[1].__class__ != DOF1:
			ErrPrnMdl (2006, "ATABL", 2, "dof1")
			raise af.LVPS_TException ("")
			
		if pl[0].__class__ != int and pl[0].__class__ != long and pl[0].__class__ != float:
			ErrPrnMdl (2004, "ATABL", 1, "float")
			raise af.LVPS_TException ("")
			
		if pl[1].__class__ != Diagram:
			ErrPrnMdl (2004, "ATABL", 2, "Diagram")
			raise af.LVPS_TException ("")

		self.this = Model ("mechanics.ATABL", nl, [pl[0], pl[1].GetTable()])
