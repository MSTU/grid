import multi
import af
import glb
import misc
import os

#import scipy

#import scipy.optimize.fmin
#import scipy.optimize.fmin_powell


from scipy.optimize import fmin
from scipy.optimize import fmin_powell



MaxValue = 1e36

class SimpleOptimization (multi.Model):

	def __init__ (self, nl, pl, desc=misc.default):
	
		self.ma = multi.Model ()
		
		self.method = pl[0]
		self.vl  = pl[1]
		self.vl0 = pl[2]
		self.fl  = pl[3]
		self.F   = pl[4]		
		
		scheme = pl[5]
		self.ma.SetScheme (scheme)
		resultfile = pl[6]
		self.ma.SetResultFile(resultfile)

				
		opensign = pl[7]
		self.ma.SetOpenSign(opensign)
		closesign = pl[8]
		self.ma.SetCloseSign(closesign)

		self.xtol = pl [9]
		self.ftol = pl[10]
		self.maxiter = pl[11]
		self.maxfun = pl[12]
					

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
		
		if self.method == 'NelderMead':
			self.xopt = fmin (self.Objective, self.vl0, xtol=self.xtol, ftol=self.ftol, maxiter=self.maxiter, maxfun=self.maxfun)
		else:
			if self.method == 'Powell':
				self.xopt = fmin_powell (self.Objective, self.vl0, xtol=self.xtol, ftol=self.ftol, maxiter=self.maxiter, maxfun=self.maxfun)
			else:
				print
				print 'SimpleOptimization Error: method ', self.method, 'is absent'
				print
#		print 'point2'
		
		self.Objective(self.xopt)	
	
	def Objective (self, x):
		self.ma.SetFilePostfix ('_opt')
		self.iteration = self.iteration + 1
		j = 1
		
#		print 'point3'
		
		for i in x:
			self.ma.SetParameterValue (j, str(i))
			self.ma.SetExtParameterValue (j, str(i))
			j = j+1
		len = j

		c = self.ma.Run()
		if c != 0:
			print 'Optimization: Error code = ', c
			return SimpleOptimization.MaxValue
		
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