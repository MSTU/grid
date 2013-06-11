from OVP import *
from structs import *

class SGMI3T (OVP):
	def __init__ (self, nl, pl):
		pl = misc.Expand (pl)

		prvpname = "mechanics.SGMI3T"
	
		if nl.__class__ != list and nl.__class__ != tuple or pl.__class__ != list and pl.__class__ != tuple:
			ErrPrnPRVP (2014, prvpname)
			raise af.LVPS_TException ("")
			
		if len (nl) != 2:
			ErrPrnPRVP (2007, prvpname, 2, len (nl))
			raise af.LVPS_TException ("")

		if len (pl) != 62:
			ErrPrnPRVP (2008, prvpname, 62, len (pl))
			raise af.LVPS_TException ("")

		for i in range(len(nl)):
			if nl[i].__class__ != OutValue:
				ErrPrnPRVP (2006, prvpname, i+1, "OutValue")
				raise af.LVPS_TException ("")
			
		for i in range(7):
			if pl[i].__class__ != pXYZ:
				ErrPrnPRVP (2004, prvpname, i+1, "pXYZ")
				raise af.LVPS_TException ("")
			
		for i in range(55):
			if pl[i+7].__class__ != int and pl[i+7].__class__ != long and pl[i+7].__class__ != float:
				ErrPrnPRVP (2004, prvpname, i+8, "float")
				raise af.LVPS_TException ("")
			
		par = []
		for i in range(7):
			Append (par, pl[i].GetList())
		Append (par, pl[7:])
			
		self.this = OVP (prvpname, nl, par)
