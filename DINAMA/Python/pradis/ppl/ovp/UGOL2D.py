from OVP import *
from structs import *

class UGOL2D (OVP):
	def __init__ (self, nl, pl):
		pl = misc.Expand (pl)

		prvpname = "mechanics.UGOL2D"
	
		if nl.__class__ != list and nl.__class__ != tuple or pl.__class__ != list and pl.__class__ != tuple:
			ErrPrnPRVP (2014, prvpname)
			raise af.LVPS_TException ("")
			
		if len (nl) != 3:
			ErrPrnPRVP (2007, prvpname, 3, len (nl))
			raise af.LVPS_TException ("")

		if len (pl) != 3:
			ErrPrnPRVP (2008, prvpname, 3, len (pl))
			raise af.LVPS_TException ("")

		for i in range(len(nl)):
			if nl[i].__class__ != XY:
				ErrPrnPRVP (2006, prvpname, i+1, "XY")
				raise af.LVPS_TException ("")
			
		for i in range(3):
			if pl[i].__class__ != pXY:
				ErrPrnPRVP (2004, prvpname, i+1, "pXY")
				raise af.LVPS_TException ("")
			
		ndl = []
		for i in range(3):
			ndl.append (nl[i].x)
			ndl.append (nl[i].y)
		par = []
		for i in range(3):
			Append (par, pl[i].GetList())
			
		self.this = OVP (prvpname, ndl, par)
