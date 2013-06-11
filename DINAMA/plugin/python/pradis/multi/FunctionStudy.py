import multi
import af
import glb
import misc
import os

class FunctionStudy (multi.FunctionStudy):

	def __init__ (self, nl, pl, desc=misc.default):
		 
		self.ma = multi.FunctionStudy ()

		 
		vl = pl[0]
		fl = pl[1]
		
		lc = pl[2]
		 
		if desc != misc.default:
			self.ma.SetScheme(desc)
		 
		vl = misc.Expand(vl)
		for i in vl:
			self.ma.AddParameter (i.Name)
			self.ma.AddExtParameter (i.Name)
		 
		fl = misc.Expand (fl)
		for i in fl:
			self.ma.AddLoadcase (i.lc)
		 
		lc = misc.Expand (lc)
		n = len(lc) / len (vl)
		 
		k = 0
		for i in range (0,n):
			self.ma.AddAnalysis()
			for j in vl:
				self.ma.AddValue (lc[k])
				k = k + 1
		
		c=self.ma.Run()
		misc.SetSolver ("")
		misc.SetPost(os.getenv("DINSYS")+"\dinama\post\Postprocessor")
		
		misc.SetPostFile(self.ma.GetHistoryFile())
						
