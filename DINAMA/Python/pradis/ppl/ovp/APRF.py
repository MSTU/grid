from OVP import *
from structs import *

class APRF (OVP):
	def __init__ (self, nl, pl):
		pl = misc.Expand (pl)

		prvpname = "mechanics.APRF"
	
		if nl.__class__ != list and nl.__class__ != tuple or pl.__class__ != list and pl.__class__ != tuple:
			ErrPrnPRVP (2014, prvpname)
			raise af.LVPS_TException ("")
			
		if len (nl) != 0:
			ErrPrnPRVP (2007, prvpname, 0, len (nl))
			raise af.LVPS_TException ("")

		if len (pl) != 9:
			ErrPrnPRVP (2008, prvpname, 9, len (pl))
			raise af.LVPS_TException ("")

		for i in range(len(pl)-1):
			if pl[i].__class__ != int and pl[i].__class__ != long and pl[i].__class__ != float:
				ErrPrnPRVP (2004, prvpname, i+1, "float")
				raise af.LVPS_TException ("")
			
		if pl[8].__class__ != Diagram:
			ErrPrnPRVP (2004, prvpname, 9, "Diagram")
			raise af.LVPS_TException ("")
			
		self.this = OVP (prvpname, nl, [pl[:8], pl[8].GetTable()])
