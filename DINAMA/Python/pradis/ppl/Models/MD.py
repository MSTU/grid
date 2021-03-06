from Model import *
from structs import *

class MD (Model):
	def __init__ (self, nl, pl):
	
		pl = misc.Expand (pl)

		if nl.__class__ != list and nl.__class__ != tuple or pl.__class__ != list and pl.__class__ != tuple:
			ErrPrnMdl (2005, "MD")
			raise af.LVPS_TException ("")
			
		if len (nl) != 1:
			ErrPrnMdl (2007, "MD", 1, len (nl))
			raise af.LVPS_TException ("")

		if len (pl) != 2:
			ErrPrnMdl (2008, "MD", 2, len (pl))
			raise af.LVPS_TException ("")

		if nl[0].__class__ != Point2d:
			ErrPrnMdl (2006, "MD", 1, "Point2d")
			raise af.LVPS_TException ("")

		if pl[0].__class__ != int and pl[0].__class__ != long and pl[0].__class__ != float:
			ErrPrnMdl (2004, "MD", 1, "float")
			raise af.LVPS_TException ("")
		
		if pl[1].__class__ != int and pl[1].__class__ != long and pl[1].__class__ != float:
			ErrPrnMdl (2004, "MD", 2, "float")
			raise af.LVPS_TException ("")
		
		self.this = Model ("mechanics.MD", nl, pl)
