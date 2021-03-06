from Model import *
from structs import *

class ATABT (Model):
	def __init__ (self, nl, pl):

		pl = misc.Expand (pl)

		if nl.__class__ != list and nl.__class__ != tuple or pl.__class__ != list and pl.__class__ != tuple:
			ErrPrnMdl (2005, "ATABT")
			raise af.LVPS_TException ("")
			
		if len (nl) != 2:
			ErrPrnMdl (2007, "ATABT", 2, len (nl))
			raise af.LVPS_TException ("")

		if len (pl) != 7:
			ErrPrnMdl (2008, "ATABT", 7, len (pl))
			raise af.LVPS_TException ("")

		if nl[0].__class__ != XY:
			ErrPrnMdl (2006, "ATABT", 1, "XY")
			raise af.LVPS_TException ("")
			
		if nl[1].__class__ != XY:
			ErrPrnMdl (2006, "ATABT", 2, "XY")
			raise af.LVPS_TException ("")
			
		if pl[0].__class__ != pXY:
			ErrPrnMdl (2004, "ATABT", 1, "pXY")
			raise af.LVPS_TException ("")
			
		if pl[1].__class__ != pXY:
			ErrPrnMdl (2004, "ATABT", 2, "pXY")
			raise af.LVPS_TException ("")
			
		if pl[2].__class__ != int and pl[2].__class__ != long and pl[2].__class__ != float:
			ErrPrnMdl (2004, "ATABT", 3, "float")
			raise af.LVPS_TException ("")
			
		if pl[3].__class__ != int and pl[3].__class__ != long and pl[3].__class__ != float:
			ErrPrnMdl (2004, "ATABT", 4, "float")
			raise af.LVPS_TException ("")
			
		if pl[4].__class__ != int and pl[4].__class__ != long and pl[4].__class__ != float:
			ErrPrnMdl (2004, "ATABT", 5, "float")
			raise af.LVPS_TException ("")
			
		if pl[5].__class__ != int and pl[5].__class__ != long and pl[5].__class__ != float:
			ErrPrnMdl (2004, "ATABT", 6, "float")
			raise af.LVPS_TException ("")
			
		if pl[6].__class__ != Diagram:
			ErrPrnMdl (2004, "ATABT", 7, "Diagram")
			raise af.LVPS_TException ("")
			
		self.this = Model ("mechanics.ATABT", nl, [pl[0].GetList(), pl[1].GetList(), pl[2:6], pl[6].GetTable])
