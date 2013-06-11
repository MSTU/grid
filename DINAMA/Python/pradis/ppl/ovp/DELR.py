from OVP import *
from structs import *

class DELR (OVP):
	def __init__ (self, nl, pl):
		pl = misc.Expand (pl)

		prvpname = "mechanics.DELR"
	
		if nl.__class__ != list and nl.__class__ != tuple or pl.__class__ != list and pl.__class__ != tuple:
			ErrPrnPRVP (2014, prvpname)
			raise af.LVPS_TException ("")
			
		if len (nl) != 2:
			ErrPrnPRVP (2007, prvpname, 2, len(nl))
			raise af.LVPS_TException ("")

		if len (pl) != 3:
			ErrPrnPRVP (2008, prvpname, 1, len (pl))
			raise af.LVPS_TException ("")

		if nl[0].__class__ != XY and nl[0].__class__ != XYZ:
			ErrPrnPRVP (2015, prvpname, 1, "XY", "XYZ")
			raise af.LVPS_TException ("")
			
		if nl[1].__class__ != nl[0].__class__:
			if nl[0].__class__ == XY:
				ErrPrnPRVP (2006, prvpname, 2, "XY")
				raise af.LVPS_TException ("")
			else:
				ErrPrnPRVP (2006, prvpname, 2, "XYZ")
				raise af.LVPS_TException ("")
			
		for i in range(2):
			if (pl[i].__class__ != pXY and nl[0].__class__ == XY) or (pl[i].__class__ != pXYZ and nl[0].__class__ == XYZ):
				if nl[0].__class__ == XY:
					ErrPrnPRVP (2004, prvpname, i+1, "pXY")
				else:
					ErrPrnPRVP (2004, prvpname, i+1, "pXYZ")
				raise af.LVPS_TException ("")
			
		if pl[2].__class__ != int and pl[2].__class__ != long and pl[2].__class__ != float:
			ErrPrnPRVP (2004, prvpname, 3, "float")
			raise af.LVPS_TException ("")
			
		if nl[0].__class__ == XY:
			ndl = [nl[0].x, nl[0].y, nl[1].x, nl[1].y]
		else:
			ndl = [nl[0].x, nl[0].y, nl[0].z, nl[1].x, nl[1].y, nl[1].z]
			
		self.this = OVP (prvpname, ndl, [pl[0].GetList(), pl[1].GetList(), pl[2]])
