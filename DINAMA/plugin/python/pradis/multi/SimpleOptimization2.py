import multi
import af
import glb
import misc
import os
import math

#import scipy

#import scipy.optimize.fmin
#import scipy.optimize.fmin_powell


from scipy.optimize import fmin
from scipy.optimize import fmin_powell



MaxValue = 1e36

class SimpleOptimization2 (multi.ModelLC):

	def __init__ (self, nl, pl, desc=misc.default):

		self.ma = multi.ModelLC ()

		self.method = pl[0]
		self.vl  = pl[1]
		self.F   = pl[3]		
		
		fl = pl[2]	
				
		self.xtol = pl [4]
		self.ftol = pl[5]
		self.maxiter = pl[6]
		self.maxfun = pl[7]
		self.A = pl[8]
		self.p = pl[9]
					

		if desc != misc.default:
			self.ma.SetScheme(desc)
			self.ma.SetDescription('Simple optimization 2: '+desc)

	
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
		
		if self.method == 'NelderMead':
			self.xopt = fmin (self.Objective, self.vl0, xtol=self.xtol, ftol=self.ftol, maxiter=self.maxiter, maxfun=self.maxfun)
		else:
			if self.method == 'Powell':
				self.xopt = fmin_powell (self.Objective, self.vl0, xtol=self.xtol, ftol=self.ftol, maxiter=self.maxiter, maxfun=self.maxfun)
			else:
				print
				print 'SimpleOptimization2 Error: method ', self.method, 'is absent'
				print
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
			return SimpleOptimization2.MaxValue
		
		value = self.F (x, self.ma)		
		
		pen = self.Penalty (x, self.bounds)
		
		value = value + pen
		
		self.ma.SetExtParameterValue (len, str(value))
		self.ma.writeHistory(self.iteration)
		
		return value
		
	def Penalty (self, x, bounds):
		
		r = 0.0
		j = 0
		for i in x:
			(min,max) =bounds [j]
			
			norm = math.fabs (self.vl0[j])
			if (min!=None):
				norm = norm + math.fabs (min)
			if (max!=None):
				norm = norm + math.fabs (max)
			norm = norm / 3.0
			if norm == 0.0:
				norm = 1.0	
			
			if min != None:
				if i<min:
					r = r + self.A *( (min- i)/norm )** self.p
			if max != None:
				if i>max:
					r = r + self.A * ((i - max)/norm) ** self.p
			j = j + 1
		
		return r