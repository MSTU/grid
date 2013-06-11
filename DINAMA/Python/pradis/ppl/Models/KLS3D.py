from Model import *
from misc import *
from structs import *
from D3SLK import D3SLK

class KLS3D (Model):
	def __init__ (self, nl, pl):

		pl = misc.Expand (pl)

		mdlname = "mechanics.KLS3D"
	
		if nl.__class__ != list and nl.__class__ != tuple or pl.__class__ != list and pl.__class__ != tuple:
			ErrPrnMdl (2005, mdlname)
			raise af.LVPS_TException ("")
			
		if len (nl) != 1:
			ErrPrnMdl (2007, mdlname, 1, len (nl))
			raise af.LVPS_TException ("")

		if len (pl) != 25:
			ErrPrnMdl (2008, mdlname, 25, len (pl))
			raise af.LVPS_TException ("")

		if nl[0].__class__ != Point:
			ErrPrnMdl (2006, mdlname, 1, "Point")
			raise af.LVPS_TException ("")

		for i in range(5):	
			if pl[i].__class__ != pXYZ:
				ErrPrnMdl (2004, mdlname, i+1, "pXYZ")
				raise af.LVPS_TException ("")
			
		for i in range(13):	
			if pl[i+5].__class__ != int and pl[i+5].__class__ != long and pl[i+5].__class__ != float:
				ErrPrnMdl (2004, mdlname, i+6, "float")
				raise af.LVPS_TException ("")
			
		for i in range(7):	
			if pl[i+18].__class__ != Diagram:
				ErrPrnMdl (2004, mdlname, i+19, "Diagram")
				raise af.LVPS_TException ("")
				
		par = []
		for i in range(5):
			Append (par, pl[i].GetList())
		Append (par, pl[5:18])
		for i in range(7):
			Append (par, pl[i+18].GetTable())
			par.append (pl[17])
		par.pop()
			
		self.this = Model (mdlname, nl, par)

		D3SLK (self, [], [])