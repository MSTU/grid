import multi
import af
import glb
import misc
import os

class MultiAnalysis (multi.MultiAnalysis):

	def __init__ (self, nl, pl, desc=misc.default):
	
		self.ma = multi.MultiAnalysis ()
		scheme = pl[0]
		self.ma.SetScheme (scheme)
		resultfile = pl[1]
		self.ma.SetResultFile(resultfile)
		
		vl = pl[2]
		fl = pl[3]
		
		lc = pl[4]
		
		opensign = pl[5]
		self.ma.SetOpenSign(opensign)
		closesign = pl[6]
		self.ma.SetCloseSign(closesign)

		if desc != misc.default:
			self.ma.SetDescription(desc)

		vl = misc.Expand(vl)
		for i in vl:
			self.ma.AddParameter (i)
		
		fl = misc.Expand (fl)
		for i in fl:
			self.ma.AddFunction (i)
		
		lc = misc.Expand (lc)
		n = len(lc) / len (vl)
		
		k = 0
		for i in range (0,n):
			self.ma.AddAnalysis()
			for j in vl:
				self.ma.AddValue (lc[k])
				k = k + 1
		
		self.ma.Run()
		misc.SetSolver ("")
		misc.SetPost(os.getenv("DINSYS")+"\dinama\post\Postprocessor")
		
		misc.SetPostFile(self.ma.GetHistoryFile())
						
