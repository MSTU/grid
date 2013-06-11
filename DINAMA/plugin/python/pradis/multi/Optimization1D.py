import multi
import af
import glb
import misc
import os

#import scipy

#import scipy.optimize.golden
#import scipy.optimize.brent


from scipy.optimize import golden
from scipy.optimize import brent
from scipy.optimize import bracket
from scipy.optimize import fminbound


MaxValue = 1e36

class Optimization1D (multi.Model):

	def __init__ (self, nl, pl, desc=misc.default):
	
		self.ma = multi.ModelLC ()
		
		self.vl  = pl[0]
		self.vl0 = self.vl.Value0
		self.fl  = pl[1]
		self.F   = pl[2]		
		self.fce = pl[3]					
		self.xtol = pl [4]
		self.maxfun = pl[5]
		self.A = pl[6]
		self.p = pl[7]
		
		
		scheme = pl[5]
		self.ma.SetScheme (scheme)
		resultfile = pl[6]
		self.ma.SetResultFile(resultfile)
				
		opensign = pl[7]
		self.ma.SetOpenSign(opensign)
		closesign = pl[8]
		self.ma.SetCloseSign(closesign)

		self.xtol = pl [9]
		self.maxfun = pl[10]

		if desc != misc.default:
			self.ma.SetDescription(desc)


	
		self.fl = misc.Expand (self.fl)
		for i in self.fl:
			self.ma.AddFunction (i)
		
		self.vl0 = misc.Expand(self.vl0)
		self.vl = misc.Expand(self.vl)
		for i in self.vl:
			self.ma.AddParameter (i)
			self.ma.AddExtParameter (i)
		self.ma.AddExtParameter ('UserFunction')
		
		self.Run()
		misc.SetSolver ("")
		misc.SetPost(os.getenv("DINSYS")+"\dinama\post\Postprocessor")
		
		misc.SetPostFile(self.ma.GetHistoryFile())
						
	def Run (self):
				
		self.iteration = 0
		self.ma.initHistory()
		
#		print 'point1'
		
		xa = self.vl0[0]
		xb = self.vl0[1]
		self.xopt = fminbound (self.Objective, xa, xb, xtol = self.xtol, maxfun = self.maxfun)



#		print 'point2'
		
		self.Objective(self.xopt)	
	
	def Objective (self, x):
		self.ma.SetFilePostfix ('_opt')
		self.iteration = self.iteration + 1
		j = 1
		
#		print 'point3'
		
		self.ma.SetParameterValue (j, str(x))
#		print j, ' ', x
		self.ma.SetExtParameterValue (j, str(x))
		j = j+1
		len = j

		c = self.ma.Run()
		if c != 0:
			print 'Optimization: Error code = ', c
			return Optimization1D.MaxValue
		
		j = 1
		f = []
		for i in self.fl:
			f = [f, self.ma.GetFunctionValue (j)]
			j = j+1
		f = misc.Expand(f)	
		value = self.F (x, f)
		
		self.ma.SetExtParameterValue (len, str(value))
		self.ma.writeHistory(self.iteration)
		
		return value