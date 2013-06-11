from Model import *
from misc import *
from structs import *
from GNIRS import GNIRS

class SRING (Model):
	def __init__ (self, nl, pl):

		pl = misc.Expand (pl)

		mdlname = "mechanics.SRING"
	
		if nl.__class__ != list and nl.__class__ != tuple or pl.__class__ != list and pl.__class__ != tuple:
			ErrPrnMdl (2005, mdlname)
			raise af.LVPS_TException ("")
			
		if len (nl) != 3:
			ErrPrnMdl (2007, mdlname, 3, len (nl))
			raise af.LVPS_TException ("")

		if len (pl) != 12:
			ErrPrnMdl (2008, mdlname, 12, len (pl))
			raise af.LVPS_TException ("")

		for i in range(3):
			if nl[i].__class__ != XYZ:
				ErrPrnMdl (2006, mdlname, i+1, "XYZ")
				raise af.LVPS_TException ("")
			
		for i in range(3):
			if pl[i].__class__ != pXYZ:
				ErrPrnMdl (2004, mdlname, i+1, "pXYZ")
				raise af.LVPS_TException ("")
			
		for i in range(7):
			if pl[i+3].__class__ != int and pl[i+3].__class__ != long and pl[i+3].__class__ != float:
				ErrPrnMdl (2004, mdlname, i+4, "float")
				raise af.LVPS_TException ("")
			
		for i in range(2):
			if pl[i+10].__class__ != Diagram:
				ErrPrnMdl (2004, mdlname, i+10, "Diagram")
				raise af.LVPS_TException ("")
			
		par = []
		for i in range(3):
			Append (par, pl[i].GetList())
		Append (par, pl[3:10])
		for i in range(2):
			Append (par, pl[10+i].GetTable())
			par.append (pl[9])
		par.pop()
		
		self.this = Model (mdlname, nl, par)

		GNIRS (self, [], [])