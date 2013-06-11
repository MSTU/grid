from OVP import *
from structs import *

class KOORD3 (OVP):
	def __init__ (self, nl, pl):
		pl = misc.Expand (pl)

		prvpname = "mechanics.KOORD3"
	
		if nl.__class__ != list and nl.__class__ != tuple or pl.__class__ != list and pl.__class__ != tuple:
			ErrPrnPRVP (2014, prvpname)
			raise af.LVPS_TException ("")
			
		if len (nl) != 1:
			ErrPrnPRVP (2007, prvpname, 1, len (nl))
			raise af.LVPS_TException ("")

		if len (pl) != 1:
			ErrPrnPRVP (2008, prvpname, 1, len (pl))
			raise af.LVPS_TException ("")

		for i in range(len(nl)):
			if nl[i].__class__ != XYZ:
				ErrPrnPRVP (2015, prvpname, i+1, "dof1", "XYZ")
				raise af.LVPS_TException ("")
			
		for i in range(len(pl)):
			if pl[i].__class__ != pXYZ:
				ErrPrnPRVP (2004, prvpname, i+1, "pXYZ")
				raise af.LVPS_TException ("")
			
		self.this = OVP (prvpname, [nl[0].x, nl[0].y, nl[0].z], pl[0].GetList())
