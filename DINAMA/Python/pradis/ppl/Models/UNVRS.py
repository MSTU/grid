from Model import *
from misc import *
from structs import *

class UNVRS (Model):
	def __init__ (self, nl, pl):

		pl = misc.Expand (pl)

		mdlname = "mechanics.UNVRS"
	
		if nl.__class__ != list and nl.__class__ != tuple or pl.__class__ != list and pl.__class__ != tuple:
			ErrPrnMdl (2005, mdlname)
			raise af.LVPS_TException ("")
			
		if len (nl) != 2:
			ErrPrnMdl (2007, mdlname, 2, len (nl))
			raise af.LVPS_TException ("")

		if len (pl) != 12:
			ErrPrnMdl (2008, mdlname, 12, len (pl))
			raise af.LVPS_TException ("")

		for i in range(2):
			if nl[i].__class__ != Point:
				ErrPrnMdl (2006, mdlname, i+1, "Point")
				raise af.LVPS_TException ("")
			
		for i in range(5):
			if pl[i].__class__ != pXYZ:
				ErrPrnMdl (2004, mdlname, i+1, "pXYZ")
				raise af.LVPS_TException ("")
			
		for i in range(3):
			if pl[i+5].__class__ != int and pl[i+5].__class__ != long and pl[i+5].__class__ != float:
				ErrPrnMdl (2004, mdlname, i+6, "float")
				raise af.LVPS_TException ("")
			
		for i in range(4):
			if pl[i+8].__class__ != Diagram:
				ErrPrnMdl (2004, mdlname, i+9, "Diagram")
				raise af.LVPS_TException ("")
			
		par = []
		for i in range(5):
			Append (par, pl[i].GetList())
		Append (par, pl[5:8])
		for i in range(4):
			Append (par, pl[8+i].GetTable())
			par.append (pl[7])
		par.pop()
		
		self.this = Model (mdlname, nl, par)
