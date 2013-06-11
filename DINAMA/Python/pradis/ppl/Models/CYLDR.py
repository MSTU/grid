from Model import *
from structs import *

class CYLDR (Model):
	def __init__ (self, nl, pl):

		pl = misc.Expand (pl)

		mdlname = "mechanics.CYLDR"
	
		if nl.__class__ != list and nl.__class__ != tuple or pl.__class__ != list and pl.__class__ != tuple:
			ErrPrnMdl (2005, mdlname)
			raise af.LVPS_TException ("")
			
		if len (nl) != 2:
			ErrPrnMdl (2007, mdlname, 2, len (nl))
			raise af.LVPS_TException ("")

		if len (pl) != 11:
			ErrPrnMdl (2008, mdlname, 11, len (pl))
			raise af.LVPS_TException ("")

		if nl[0].__class__ != Point:
			ErrPrnMdl (2006, mdlname, 1, "Point")
			raise af.LVPS_TException ("")
			
		if nl[1].__class__ != Point:
			ErrPrnMdl (2006, mdlname, 2, "Point")
			raise af.LVPS_TException ("")
			
		for i in range(4):
			if pl[i].__class__ != pXYZ:
				ErrPrnMdl (2004, mdlname, i+1, "pXYZ")
				raise af.LVPS_TException ("")

		for i in range(3):
			if pl[4+i].__class__ != int and pl[4+i].__class__ != long and pl[4+i].__class__ != float:
				ErrPrnMdl (2004, mdlname, 5+i, "float")
				raise af.LVPS_TException ("")
			
		for i in range(4):
			if pl[i+7].__class__ != Diagram:
				ErrPrnMdl (2004, mdlname, i+8, "Diagram")
				raise af.LVPS_TException ("")
			
		self.this = Model (mdlname, nl, [pl[0].GetList(), pl[1].GetList(), 
						 pl[2].GetList(), pl[3].GetList(),
						 pl[4:7], pl[7].GetTable(), pl[6],
						 pl[8].GetTable(), pl[6],
						 pl[9].GetTable(), pl[6],
						 pl[10].GetTable()])
