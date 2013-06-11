from OVP import *
from structs import *

class PROXL (OVP):
	def __init__ (self, nl, pl):
		pl = misc.Expand (pl)

		prvpname = "mechanics.PROXL"
	
		if nl.__class__ != list and nl.__class__ != tuple or pl.__class__ != list and pl.__class__ != tuple:
			ErrPrnPRVP (2014, prvpname)
			raise af.LVPS_TException ("")
			
		if len (nl) != 3:
			ErrPrnPRVP (2007, prvpname, 3, len (nl))
			raise af.LVPS_TException ("")

		if len (pl) != 3:
			ErrPrnPRVP (2008, prvpname, 5, len (pl))
			raise af.LVPS_TException ("")

		for i in range(len(nl)):
			if nl[i].__class__ != XY:
				ErrPrnPRVP (2006, prvpname, i+1, "XY")
				raise af.LVPS_TException ("")
			
		for i in range(2):
			if pl[i].__class__ != pXY:
				ErrPrnPRVP (2004, prvpname, i+1, "pXY")
				raise af.LVPS_TException ("")
			
		for i in range(1):
			if pl[i+2].__class__ != int and pl[i+2].__class__ != long and pl[i+2].__class__ != float:
				ErrPrnPRVP (2004, prvpname, i+3, "float")
				raise af.LVPS_TException ("")
				
		ndl = []
		for i in range(3):
			ndl.append (nl[i].x)
			ndl.append (nl[i].y)
		par = []
		for i in range(2):
			Append (par, pl[i].GetList())
		Append (par, pl[2:])
			
		self.this = OVP (prvpname, ndl, par)
