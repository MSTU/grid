import multi
import af
import glb
import misc
import os

#import scipy

#import scipy.optimize.lbfgsb


from scipy.optimize.lbfgsb import fmin_l_bfgs_b



MaxValue = 1e36

class LBFGSB (multi.ModelLC):

	def __init__ (self, nl, pl, desc=misc.default):
	
		self.ma = multi.ModelLC ()
		
		self.vl  = pl[0]
		self.F   = pl[2]		
		
		fl = pl[1]	
				
		self.m = pl [3]
		self.factr = pl[4]
		self.pgtol = pl[5]
		self.epsilon = pl[6]
		self.maxfun = pl[7]
					

		if desc != misc.default:
			self.ma.SetScheme(desc)
			self.ma.SetDescription('LBFGSB optimization: '+desc)

	
		fl = misc.Expand (fl)
		for i in fl:
			self.ma.AddLoadcase (i.lc)
		
		self.vl = misc.Expand(self.vl)
		self.vl0 = []
		self.bounds = []
		for i in self.vl:
			self.ma.AddParameter (i.Name)
			self.ma.AddExtParameter (i.Name)
			self.vl0.append (i.Value0)
			self.bounds.append ((i.Min, i.Max))
			
		self.ma.AddExtParameter ('Objective')
		
		self.Run()
		misc.SetSolver ("")
		misc.SetPost(os.getenv("DINSYS")+"\dinama\post\Postprocessor")
		
		misc.SetPostFile(self.ma.GetHistoryFile())
						
	def Run (self):
				
		self.iteration = 0
		self.ma.initHistory()
		
#		print 'point1'
		
		(self.xopt, f, d) = fmin_l_bfgs_b (self.Objective, self.vl0, approx_grad=1, bounds = self.bounds, m = self.m, factr=self.factr, pgtol=self.pgtol, epsilon=self.epsilon, maxfun=self.maxfun)
#		print 'point2'
		
		self.Objective(self.xopt)	
	
	def Objective (self, x):
		self.ma.SetFilePostfix ('_opt')
		self.iteration = self.iteration + 1
		j = 0
		
#		print 'point3'
		
		for i in x:
			self.ma.SetParameterValue (j, str(i))
			self.ma.SetExtParameterValue (j, str(i))
			j = j+1
		len = j

		c = self.ma.Run()
		if c != 0:
			print 'Optimization: Error code = ', c
			return LBFGSB.MaxValue
		
			
		value = self.F (x, self.ma)
		
		self.ma.SetExtParameterValue (len, str(value))
		self.ma.writeHistory(self.iteration)
		
		return value