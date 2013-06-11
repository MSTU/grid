from Image import *
from structs import *

class DOTD (Image):
	def __init__ (self, model, pl, lp):
		pl = misc.Expand (pl)

		pgoname = "mechanics.DOTD"
	
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

		if pl[0].__class__ != pXY:
			ErrPrnPGO (2004, pgoname, 1, "pXY")
			raise af.LVPS_TException ("")
			
		for i in range(2):
			if pl[i+1].__class__ != int and pl[i+1].__class__ != long and pl[i+1].__class__ != float:
				ErrPrnPGO (2004, pgoname, i+2, "float")
				raise af.LVPS_TException ("")
			
		self.this = Image (model, pgoname, [pl[0].GetList(), pl[1:]], lp)
