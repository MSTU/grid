from Image import *
from structs import *

class PRUG (Image):
	def __init__ (self, model, pl, lp):
		pl = misc.Expand (pl)

		pgoname = "mechanics.PRUG"
	
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
			
		if len (pl) != 2:
			ErrPrnPGO (2008, pgoname, 2, len (pl))
			raise af.LVPS_TException ("")

		for i in range(len(pl)):
			if pl[i].__class__ != int and pl[i].__class__ != long and pl[i].__class__ != float:
				ErrPrnPGO (2004, pgoname, i+1, "float")
				raise af.LVPS_TException ("")
			
		self.this = Image (model, pgoname, pl, lp)
