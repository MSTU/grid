import af
import glb

default = 17777.0

class Print (af.Print):

	def __init__ (self, rnglist, 
			start = default,
			end = default,
			frm = default,
			scale = default, 
			desc=default):
		
		pl = glb.sch.GetPrintList ()
		self.this = af.Print (pl.Add())
		rl = af.TList (self.SetRangeList())
		for i in rnglist:
			rl.Add (i)
		pl = af.TList (self.SetParameterList())
		if start != default:
			dt = af.TReal (pl.Add())
			dt.SetName ('START')
			dt.SetValue (start)
		if end != default:
			dt = af.TReal (pl.Add())
			dt.SetName ('END')
			dt.SetValue (end)
		if frm != default:
			dt = af.TReal (pl.Add())
			dt.SetName ('FROM')
			dt.SetValue (frm)
		if scale != default:
			dt = af.TReal (pl.Add())
			dt.SetName ('SCALE')
			dt.SetValue (scale)
		if desc != default:
			self.SetDescription(desc)

