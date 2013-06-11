import af
from Model import *
from Image import *
from OVP import *
from Solver import *
from Print import *

default = 17777.0

class Scheme (af.Scheme):
	
#	def init ():
#	Desc="11"
	def __init__ (self, desc=misc.default):
#		fmtlist = glb.sch.GetFragmentList()
		fmtlist = glb.sch_main.GetFragmentList()
		self.this = af.Scheme (fmtlist.Add())
		if desc != misc.default:
			self.SetDescription(desc)
#		self.SetObjectName("Scheme")	
		self.SetDataList ()
		self.SetModelList ()
		self.SetImageList ()
		self.SetOutVariableList ()
		self.SetRunList ()
		self.SetPrintList ()
		self.SetFragmentList ()
		self.SetIncludeList()
		glb.sch_list.append (glb.sch)
		glb.sch = self
#		setattr(self,"Desc",desc)
		self.Desc = desc

	def begin (self):
		glb.sch_list.append (glb.sch)
		glb.sch = self
	
	def end (self):
		glb.sch = glb.sch_list.pop ()
	
	def GetSchemeName(self):
#		print "desc=",self.Desc
#		print "desc2 = ", af.Scheme.GetDescription(self)
		return self.Desc
	
	def AddModel (self, name, nl, pl):
		mdlist = self.GetModelList()
		mdl = Model (mdlist.Add())
		mdl.SetObjectName (name)
		prmlist = af.TList (mdl.SetParameterList())
		for i in pl:
			prm = af.TReal (prmlist.Add())
			prm.SetValue (i)
		ndlist = af.TList (mdl.SetNodeList())
		for i in nl:
			ndlist.Add(i)
		return mdl
		
	def AddOVP (self, prvp, nl, pl):
		ovplist = self.GetOutVariableList()
		ovp = OVP (ovplist.Add())
		ovp.SetObjectName (prvp)
		prmlist = af.TList (ovp.SetParameterList())
		for i in pl:
			prm = af.TReal (prmlist.Add())
			prm.SetValue (i)
		OVList = af.TList (ovp.SetOutValueList())
		hlp = OutValue ()
		for i in nl:
			ov = af.OutValue (OVList.Add())
			if hlp.__class__ != i.__class__ :
				ov.SetOutValueType (1)
				ov.SetNodeOfValue (i)
			else:
				ov.SetOutValueType (i.type)
				if i.type == 2 or i.type == 3:
					ov.SetNodeOfValue (i.node)
				else:
					ov.SetNumber (i.number)
					ov.SetModelOfValue (i.model)
		return ovp
	
	def AddImage (self, model, pgo, pgoparams, lp):
		ilist = self.GetImageList()
		img = Image (ilist.Add())
		img.SetObjectName (pgo)
		img.SetImageModel (model)
		pl = af.TList (img.SetParameterList())
		for i in pgoparams:
			r = af.TReal (pl.Add())
			r.SetValue (i)
		layer = af.Layer (img.SetLayerParameters())
		layer.SetColor (lp[0])
		layer.SetMaterial (lp[1])
		layer.SetTransparency (lp[2])
		return img
		
	def AddSolver (self, name, rnglist, 
			save 	= default,   
			end 	= default,    
			out 	= default,    
			smax 	= default,   
			smin 	= default,
			drlti 	= default,  
			dabsi 	= default,  
			drltu 	= default,  
			dabsu 	= default,  
			drltx 	= default,
			dabsx 	= default,  
			flag 	= default,   
			itr 	= default,    
			debug 	= default,  
			optim 	= default,
			control 	= default, 
			mode 	= default,   
			change 	= default,
			outs 	= default,   
			predict 	= default, 
			scheme 	= default, 
			weight 	= default, 
			second 	= default,
			ignore 	= default,
			atm 	= default,
			scale 	= default,  
			checkm 	= default, 
			outper 	= default, 
			outvar 	= default,	
			prttime = default,
			rlmin 	= default,  
			msheps 	= default, 
			parerr 	= default, 
			pspprt 	= default, 
			err 	= default):
			
		sl = self.GetRunList()
		solver = Solver (sl.Add())
		solver.SetObjectName (name)
		rl = af.TList (solver.SetRangeList())
		for i in rnglist:
			rl.Add (i)
		pl = af.TList (solver.SetParameterList())
		dt = af.TReal (pl.Add())
		dt.SetName ('SAVE')
		dt.SetValue (save)
		dt = af.TReal (pl.Add())
		dt.SetName ('END')
		dt.SetValue (end)
		dt = af.TReal (pl.Add())
		dt.SetName ('OUT')
		dt.SetValue (out)
		dt = af.TReal (pl.Add())
		dt.SetName ('SMAX')
		dt.SetValue (smax)
		dt = af.TReal (pl.Add())
		dt.SetName ('SMIN')
		dt.SetValue (smin)
		dt = af.TReal (pl.Add())
		dt.SetName ('DRLTI')
		dt.SetValue (drlti)
		dt = af.TReal (pl.Add())
		dt.SetName ('DABSI')
		dt.SetValue (dabsi)
		dt = af.TReal (pl.Add())
		dt.SetName ('DRLTU')
		dt.SetValue (drltu)
		dt = af.TReal (pl.Add())
		dt.SetName ('DABSU')
		dt.SetValue (dabsu)
		dt = af.TReal (pl.Add())
		dt.SetName ('DRLTX')
		dt.SetValue (drltx)
		dt = af.TReal (pl.Add())
		dt.SetName ('DABSX')
		dt.SetValue (dabsx)
		dt = af.TReal (pl.Add())
		dt.SetName ('FLAG')
		dt.SetValue (flag)
		dt = af.TReal (pl.Add())
		dt.SetName ('ITR')
		dt.SetValue (itr)
		dt = af.TReal (pl.Add())
		dt.SetName ('DEBUG')
		dt.SetValue (debug)
		dt = af.TReal (pl.Add())
		dt.SetName ('OPTIM')
		dt.SetValue (optim)
		#dt = af.TReal (pl.Add())
		#dt.SetName ('CONTROL')
		#dt.SetValue (control)
		dt = af.TReal (pl.Add())
		dt.SetName ('MODE')
		dt.SetValue (mode)
		dt = af.TReal (pl.Add())
		dt.SetName ('CHANGE')
		dt.SetValue (change)
		dt = af.TReal (pl.Add())
		dt.SetName ('OUTS')
		dt.SetValue (outs)
		#dt = af.TReal (pl.Add())
		#dt.SetName ('PREDICT')
		#dt.SetValue (predict)
		dt = af.TReal (pl.Add())
		dt.SetName ('SCHEME')
		dt.SetValue (scheme)
		dt = af.TReal (pl.Add())
		dt.SetName ('WEIGHT')
		dt.SetValue (weight)
		dt = af.TReal (pl.Add())
		dt.SetName ('SECOND')
		dt.SetValue (second)
		dt = af.TReal (pl.Add())
		dt.SetName ('IGNORE')
		dt.SetValue (ignore)
		dt = af.TReal (pl.Add())
		dt.SetName ('ATM')
		dt.SetValue (atm)
		dt = af.TReal (pl.Add())
		dt.SetName ('SCALE')
		dt.SetValue (scale)
		dt = af.TReal (pl.Add())
		dt.SetName ('CHECKM')
		dt.SetValue (checkm)
		dt = af.TReal (pl.Add())
		dt.SetName ('OUTPER')
		dt.SetValue (outper)
		dt = af.TReal (pl.Add())
		dt.SetName ('OUTVAR')
		dt.SetValue (outvar)
		dt = af.TReal (pl.Add())
		dt.SetName ('PRTTIME')
		dt.SetValue (prttime)
		#dt = af.TReal (pl.Add())
		#dt.SetName ('RLMIN')
		#dt.SetValue (rlmin)
		#dt = af.TReal (pl.Add())
		#dt.SetName ('MSHEPS')
		#dt.SetValue (msheps)
		#dt = af.TReal (pl.Add())
		#dt.SetName ('PARERR')
		#dt.SetValue (parerr)
		#dt = af.TReal (pl.Add())
		#dt.SetName ('PSPPRT')
		#dt.SetValue (pspprt)
		#dt = af.TReal (pl.Add())
		#dt.SetName ('ERR')
		#dt.SetValue (err)
		return solver
		
	def AddPrint (self, rnglist, 
			start = default,
			end = default,
			frm = default,
			scale = default):
			
		pl = self.GetPrintList ()
		prn = Print (pl.Add())
		rl = af.TList (prn.SetRangeList())
		for i in rnglist:
			rl.Add (i)
		pl = af.TList (prn.SetParameterList())
		dt = af.TReal (pl.Add())
		dt.SetName ('START')
		dt.SetValue (start)
		dt = af.TReal (pl.Add())
		dt.SetName ('END')
		dt.SetValue (end)
		dt = af.TReal (pl.Add())
		dt.SetName ('FROM')
		dt.SetValue (frm)
		dt = af.TReal (pl.Add())
		dt.SetName ('SCALE')
		dt.SetValue (scale)
		return prn
		
