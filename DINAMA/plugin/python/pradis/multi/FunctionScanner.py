import multi
import af
import glb
import misc
import os

class FunctionScanner (multi.FunctionScanner):

	def __init__ (self, nl, pl, desc=misc.default):
		 
		self.ma = multi.FunctionScanner ()

		 
		vl = pl[0]
		rl = pl[1]
		
		fl = pl[2]
		 
		if desc != misc.default:
			self.ma.SetScheme(desc)
		 
		vl = misc.Expand(vl)
		n = 0
		for i in vl:
			var = multi.Variable()
			var.Name = i.Name
			var.Value0 = i.Value0
			if (i.Min != None):
				var.Min = i.Min
			else:
				var.Min = i.Value0
			if (i.Max != None):
				var.Max = i.Max
			else:
				var.Max = i.Value0
			
			if (n < len(rl)):
				var.Count = rl[n]
			else:
				var.Count = 1
			
			self.ma.AddVariable (var)
			n = n + 1
#			print var

		 
		fl = misc.Expand (fl)
		for i in fl:
			self.ma.AddLoadcase (i.lc)
		 		 

		c=self.ma.Run()
		misc.SetSolver ("")
		misc.SetPost(os.getenv("DINSYS")+"\dinama\post\Postprocessor")
		
		misc.SetPostFile(self.ma.GetHistoryFile())
						
