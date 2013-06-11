from OVP import *
from structs import *

class SPA3L (OVP):
	def __init__ (self, nl, pl):
		pl = misc.Expand (pl)

		prvpname = "mechanics.SPA3L"
	
		if nl.__class__ != list and nl.__class__ != tuple or pl.__class__ != list and pl.__class__ != tuple:
			ErrPrnPRVP (2014, prvpname)
			raise af.LVPS_TException ("")
			
		if len (nl) != 2:
			ErrPrnPRVP (2007, prvpname, 2, len (nl))
			raise af.LVPS_TException ("")

		if len (pl) != 5:
			ErrPrnPRVP (2008, prvpname, 5, len (pl))
			raise af.LVPS_TException ("")

		for i in range(len(nl)):
			if nl[i].__class__ != DOF and nl[i].__class__ != DOF1 and nl[i].__class__ != OutValue:
				ErrPrnPRVP (2006, prvpname, i+1, "XYZ")
				raise af.LVPS_TException ("")
			
		for i in range(5):
			if pl[i].__class__ != pXYZ:
				ErrPrnPRVP (2004, prvpname, i+1, "pXYZ")
				raise af.LVPS_TException ("")
			
		par = []
		for i in range(5):
			Append (par, pl[i].GetList())
			
		self.this = OVP (prvpname, nl, par)
