from OVP import *
from structs import *

class FIA (OVP):
	def __init__ (self, nl, pl):
		pl = misc.Expand (pl)

		prvpname = "mechanics.FIA"
	
		if nl.__class__ != list and nl.__class__ != tuple or pl.__class__ != list and pl.__class__ != tuple:
			ErrPrnPRVP (2014, prvpname)
			raise af.LVPS_TException ("")
			
		if len (nl) != 2:
			ErrPrnPRVP (2007, prvpname, 2, len (nl))
			raise af.LVPS_TException ("")

		if len (pl) != 3:
			ErrPrnPRVP (2008, prvpname, 3, len (pl))
			raise af.LVPS_TException ("")

		for i in range(len(nl)):
			if nl[i].__class__ != XY:
				ErrPrnPRVP (2006, prvpname, i+1, "XY")
				raise af.LVPS_TException ("")
			
		for i in range(2):
			if pl[i].__class__ != pXY:
				ErrPrnPRVP (2004, prvpname, i+1, "pXY")
				raise af.LVPS_TException ("")
			
		if pl[2].__class__ != int and pl[2].__class__ != long and pl[2].__class__ != float:
			ErrPrnPRVP (2004, prvpname, 5, "float")
			raise af.LVPS_TException ("")
			
		self.this = OVP (prvpname, [nl[0].x, nl[0].y, nl[1].x, nl[1].y], [pl[0].GetList(), pl[1].GetList(), pl[2]])
