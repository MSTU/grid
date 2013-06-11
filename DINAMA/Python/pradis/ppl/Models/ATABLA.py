from Model import *
from structs import *

class ATABLA (Model):
	def __init__ (self, nl, pl):

		pl = misc.Expand (pl)

		if nl.__class__ != list and nl.__class__ != tuple or pl.__class__ != list and pl.__class__ != tuple:
			ErrPrnMdl (2005, "ATABLA")
			raise af.LVPS_TException ("")
			
		if len (nl) != 2:
			ErrPrnMdl (2007, "ATABLA", 2, len (nl))
			raise af.LVPS_TException ("")

		if len (pl) < 2 or len (pl) > 6:
			ErrPrnMdl (2009, "ATABLA", 2, 6, len (pl))
			raise af.LVPS_TException ("")

		if nl[0].__class__ != DOF and nl[0].__class__ != DOF1:
			ErrPrnMdl (2006, "ATABLA", 1, "dof1")
			raise af.LVPS_TException ("")
			
		if nl[1].__class__ != DOF and nl[1].__class__ != DOF1:
			ErrPrnMdl (2006, "ATABLA", 2, "dof1")
			raise af.LVPS_TException ("")
			
		if pl[0].__class__ != int and pl[0].__class__ != long and pl[0].__class__ != float:
			ErrPrnMdl (2004, "ATABLA", 1, "float")
			raise af.LVPS_TException ("")
			
		if pl[1].__class__ != Diagram:
			ErrPrnMdl (2004, "ATABLA", 2, "Diagram")
			raise af.LVPS_TException ("")
			
		if len (pl) > 2:
			if pl[2].__class__ != int and pl[2].__class__ != long and pl[2].__class__ != float:
				ErrPrnMdl (2004, "ATABLA", 3, "float")
				raise af.LVPS_TException ("")
			
		if len (pl) > 3:
			if pl[3].__class__ != int and pl[3].__class__ != long and pl[3].__class__ != float:
				ErrPrnMdl (2004, "ATABLA", 4, "float")
				raise af.LVPS_TException ("")
			
		if len (pl) > 4:
			if pl[4].__class__ != int and pl[4].__class__ != long and pl[4].__class__ != float:
				ErrPrnMdl (2004, "ATABLA", 5, "float")
				raise af.LVPS_TException ("")
			
		if len (pl) > 5:
			if pl[5].__class__ != int and pl[5].__class__ != long and pl[5].__class__ != float:
				ErrPrnMdl (2004, "ATABLA", 6, "float")
				raise af.LVPS_TException ("")
			
		self.this = Model ("mechanics.ATABLA", nl, [pl[0], pl[1].GetTable(), pl[2:]])
