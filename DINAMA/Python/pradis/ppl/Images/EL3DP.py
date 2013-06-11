from Image import *
from misc import *
from structs import *

class EL3DP (Image):
	def __init__ (self, model, pl, lp):
		pl = misc.Expand (pl)

		pgoname = "mechanics.EL3DP"
	
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
			
		if len (pl) != 8:
			ErrPrnPGO (2008, pgoname, 8, len (pl))
			raise af.LVPS_TException ("")

		for i in range(5):
			if pl[i].__class__ != pXYZ:
				ErrPrnPGO (2004, pgoname, i+1, "pXYZ")
				raise af.LVPS_TException ("")
			
		for i in range(3):
			if pl[i+5].__class__ != int and pl[i+5].__class__ != long and pl[i+5].__class__ != float:
				ErrPrnPGO (2004, pgoname, i+6, "float")
				raise af.LVPS_TException ("")
			
		par = []
		for i in range(5):
			Append (par, pl[i].GetList())
		Append (par, pl[5:])
				
		self.this = Image (model, pgoname, par, lp)
