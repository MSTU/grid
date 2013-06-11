from Image import *
from structs import *

class POINT (Image):
	def __init__ (self, model, pl, lp):
		pl = misc.Expand (pl)

		pgoname = "mechanics.POINT"
	
		ddd = dir(model)
		if ddd.count("GetName") == 0:
			ErrPrnPGO (2023, pgoname)
			raise af.LVPS_TException ("")
	
		if model.GetName() != "Model":
			ErrPrnPGO (2023, pgoname)
			raise af.LVPS_TException ("")

		if pl.__class__ != list and pl.__class__ != tuple:
			ErrPrnPGO (2022, pgoname)
			raise af.LVPS_TException ("")
			
		if len (pl) != 3:
			ErrPrnPGO (2008, pgoname, 3, len (pl))
			raise af.LVPS_TException ("")

		for i in range(1):
			if pl[i].__class__ != pXYZ:
				ErrPrnPGO (2004, pgoname, i+1, "pXYZ")
				raise af.LVPS_TException ("")
			
		for i in range(len(pl)-1):
			if pl[i+1].__class__ != int and pl[i+1].__class__ != long and pl[i+1].__class__ != float:
				ErrPrnPGO (2004, pgoname, i+2, "float")
				raise af.LVPS_TException ("")
			
		par = []
		for i in range(1):
			misc.Append (par, pl[i].GetList())
		misc.Append (par, pl[1:])
				
		self.this = Image (model, pgoname, par, lp)
