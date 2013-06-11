import af
import glb
import misc

default = 17777.0

class Solver (af.Solver):

	def __init__ (self, name, rnglist, 
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
			err 	= default,
			desc=default):
		
		sl = glb.sch.GetRunList()
		self.this = af.Solver (sl.Add())
		if desc != default:
			self.SetDescription(desc)
		self.SetObjectName (name)
		rl = af.TList (self.SetRangeList())
		for i in rnglist:
			rl.Add (i)
		pl = af.TList (self.SetParameterList())
		if save != default:
			dt = af.TReal (pl.Add())
			dt.SetName ('SAVE')
			dt.SetValue (save)
		if end != default:
			dt = af.TReal (pl.Add())
			dt.SetName ('END')
			dt.SetValue (end)
		if out != default:
			dt = af.TReal (pl.Add())
			dt.SetName ('OUT')
			dt.SetValue (out)
		if smax != default:
			dt = af.TReal (pl.Add())
			dt.SetName ('SMAX')
			dt.SetValue (smax)
		if smin != default:
			dt = af.TReal (pl.Add())
			dt.SetName ('SMIN')
			dt.SetValue (smin)
		if drlti != default:
			dt = af.TReal (pl.Add())
			dt.SetName ('DRLTI')
			dt.SetValue (drlti)
		if dabsi != default:
			dt = af.TReal (pl.Add())
			dt.SetName ('DABSI')
			dt.SetValue (dabsi)
		if drltu != default:
			dt = af.TReal (pl.Add())
			dt.SetName ('DRLTU')
			dt.SetValue (drltu)
		if dabsu != default:
			dt = af.TReal (pl.Add())
			dt.SetName ('DABSU')
			dt.SetValue (dabsu)
		if drltx != default:
			dt = af.TReal (pl.Add())
			dt.SetName ('DRLTX')
			dt.SetValue (drltx)
		if dabsx != default:
			dt = af.TReal (pl.Add())
			dt.SetName ('DABSX')
			dt.SetValue (dabsx)
		if flag != default:
			dt = af.TReal (pl.Add())
			dt.SetName ('FLAG')
			dt.SetValue (flag)
		if itr != default:
			dt = af.TReal (pl.Add())
			dt.SetName ('ITR')
			dt.SetValue (itr)
		if debug != default:
			dt = af.TReal (pl.Add())
			dt.SetName ('PREDICT')
			dt.SetValue (predict)
		if debug != default:
			dt = af.TReal (pl.Add())
			dt.SetName ('DEBUG')
			dt.SetValue (debug)
		if optim != default:
			dt = af.TReal (pl.Add())
			dt.SetName ('OPTIM')
			dt.SetValue (optim)
		if control != default:
			dt = af.TReal (pl.Add())
			dt.SetName ('CONTROL')
			dt.SetValue (control)
		if mode != default:
			dt = af.TReal (pl.Add())
			dt.SetName ('MODE')
			dt.SetValue (mode)
		if change != default:
			dt = af.TReal (pl.Add())
			dt.SetName ('CHANGE')
			dt.SetValue (change)
		if outs != default:
			dt = af.TReal (pl.Add())
			dt.SetName ('OUTS')
			dt.SetValue (outs)
		if scheme != default:
			dt = af.TReal (pl.Add())
			dt.SetName ('SCHEME')
			dt.SetValue (scheme)
		if weight != default:
			dt = af.TReal (pl.Add())
			dt.SetName ('WEIGHT')
			dt.SetValue (weight)
		if second != default:
			dt = af.TReal (pl.Add())
			dt.SetName ('SECOND')
			dt.SetValue (second)
		if ignore != default:
			dt = af.TReal (pl.Add())
			dt.SetName ('IGNORE')
			dt.SetValue (ignore)
		if atm != default:
			dt = af.TReal (pl.Add())
			dt.SetName ('ATM')
			dt.SetValue (atm)
		if scale != default:
			dt = af.TReal (pl.Add())
			dt.SetName ('SCALE')
			dt.SetValue (scale)
		if checkm != default:
			dt = af.TReal (pl.Add())
			dt.SetName ('CHECKM')
			dt.SetValue (checkm)
		if outper != default:
			dt = af.TReal (pl.Add())
			dt.SetName ('OUTPER')
			dt.SetValue (outper)
		if outvar != default:
			dt = af.TReal (pl.Add())
			dt.SetName ('OUTVAR')
			dt.SetValue (outvar)
		if prttime != default:
			dt = af.TReal (pl.Add())
			dt.SetName ('PRTTIME')
			dt.SetValue (prttime)
		misc.SetSlang()
