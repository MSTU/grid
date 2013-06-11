from Image import *
from structs import *

class CIL3DC (Image):
	def __init__ (self, model, pl, lp):
		pl = misc.Expand (pl)

		pgoname = "mechanics.CIL3DC"
	
		if pl.__class__ != list and pl.__class__ != tuple:
			ErrPrnPGO (2022, pgoname)
			raise af.LVPS_TException ("")
		
		ddd = dir(model)
		ismdl = 1
		if ddd.count("GetName") == 0:
			ismdl = 0
		if ismdl == 1:
			if model.GetName() != "Model":
				ismdl = 0
	
		if ismdl == 0:
			if len(pl) < 5 or len(pl)>6:
				ErrPrnPGO (2016, len(pl), 5, 6)
				raise af.LVPS_TException ("")
			for i in range(2):
				if pl[i].__class__ != pXYZ:
					ErrPrnPGO (2004, i+1, "pXYZ")
					raise af.LVPS_TException ("")
			for i in range(len(pl)-2):
				if pl[i+2].__class__ != int and pl[i+2].__class__ != long and pl[i+2].__class__ != float:
					ErrPrnPGO (2004, i+3, "float")
					raise af.LVPS_TException ("")
			par = [pl[0].GetList(), pl[1].GetList(), pl[2:]]
		else:
				
			mdl = model.GetObjectName()

			if mdl == "MJ3D" or mdl[:3] == "SV3":
				if len(pl) < 3 or len(pl)>4:
					ErrPrnPGO (2016, len(pl), 3, 4)
					raise af.LVPS_TException ("")
				for i in range(len(pl)):
					if pl[i].__class__ != int and pl[i].__class__ != long and pl[i].__class__ != float:
						ErrPrnPGO (2004, i+1, "float")
						raise af.LVPS_TException ("")
				par = pl
			else:
				if len(pl) < 0 or len(pl)>4:
					ErrPrnPGO (2016, len(pl), 0, 4)
					raise af.LVPS_TException ("")
				for i in range(len(pl)):
					if pl[i].__class__ != int and pl[i].__class__ != long and pl[i].__class__ != float:
						ErrPrnPGO (2004, i+1, "float")
						raise af.LVPS_TException ("")
				par = pl
		
		self.this = Image (model, pgoname, par, lp)
