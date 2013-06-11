from OVP import *
from structs import *

class DX (OVP):
	def __init__ (self, nl, pl):
		pl = misc.Expand (pl)

		prvpname = "mechanics.DX"
	
		if nl.__class__ != list and nl.__class__ != tuple or pl.__class__ != list and pl.__class__ != tuple:
			ErrPrnPRVP (2014, prvpname)
			raise af.LVPS_TException ("")
			
		if len (nl) != 2:
			ErrPrnPRVP (2007, prvpname, 2, len (nl))
			raise af.LVPS_TException ("")

		if len (pl) != 1:
			ErrPrnPRVP (2008, prvpname, 1, len (pl))
			raise af.LVPS_TException ("")

		for i in range(len(nl)):
			if nl[i].__class__ != DOF and nl[i].__class__ != DOF1 and nl[i].__class__ != OutValue:
				ErrPrnPRVP (2015, prvpname, i+1, "dof1", "OutValue")
				raise af.LVPS_TException ("")
			
		for i in range(len(pl)):
			if pl[i].__class__ != int and pl[i].__class__ != long and pl[i].__class__ != float:
				ErrPrnPRVP (2004, prvpname, i+1, "float")
				raise af.LVPS_TException ("")
			
		self.this = OVP (prvpname, nl, pl)
