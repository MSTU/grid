from OVP import *
from structs import *

class DFIA (OVP):
	def __init__ (self, nl, pl):
		pl = misc.Expand (pl)

		prvpname = "mechanics.DFIA"
	
		if nl.__class__ != list and nl.__class__ != tuple or pl.__class__ != list and pl.__class__ != tuple:
			ErrPrnPRVP (2014, prvpname)
			raise af.LVPS_TException ("")
			
		if len (nl) != 4:
			ErrPrnPRVP (2007, prvpname, 4, len (nl))
			raise af.LVPS_TException ("")

		if len (pl) != 5:
			ErrPrnPRVP (2008, prvpname, 5, len (pl))
			raise af.LVPS_TException ("")

		for i in range(len(nl)):
			if nl[i].__class__ != XY:
				ErrPrnPRVP (2006, prvpname, i+1, "XY")
				raise af.LVPS_TException ("")
			
		for i in range(4):
			if pl[i].__class__ != pXY:
				ErrPrnPRVP (2004, prvpname, i+1, "pXY")
				raise af.LVPS_TException ("")
			
		if pl[4].__class__ != int and pl[4].__class__ != long and pl[4].__class__ != float:
			ErrPrnPRVP (2004, prvpname, 5, "float")
			raise af.LVPS_TException ("")
			
		self.this = OVP (prvpname, [nl[0].x, nl[0].y, nl[1].x, nl[1].y, nl[2].x, nl[2].y, nl[3].x, nl[3].y], [pl[0].GetList(), pl[1].GetList(), pl[2].GetList(), pl[3].GetList(), pl[4]])
