from OVP import *
from misc import *
from structs import *

class DFIB (OVP):
	def __init__ (self, nl, pl):
		pl = misc.Expand (pl)

		prvpname = "mechanics.DFIB"
	
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
			if nl[i].__class__ != XYZ:
				ErrPrnPRVP (2006, prvpname, i+1, "XYZ")
				raise af.LVPS_TException ("")
			
		for i in range(4):
			if pl[i].__class__ != pXYZ:
				ErrPrnPRVP (2004, prvpname, i+1, "pXYZ")
				raise af.LVPS_TException ("")
			
		if pl[4].__class__ != int and pl[4].__class__ != long and pl[4].__class__ != float:
			ErrPrnPRVP (2004, prvpname, 5, "float")
			raise af.LVPS_TException ("")
			
		ndl = []
		for i in range(4):
			ndl.append (nl[i].x)
			ndl.append (nl[i].y)
			ndl.append (nl[i].z)
			
		par = []
		for i in range(4):
			Append (par, pl[i].GetList())
		par.append (pl[4])
			
		self.this = OVP (prvpname, ndl, par)
