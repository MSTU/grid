import multi
import af
import glb
import misc
import os
import math
import numpy
#import scipy



from scipy.optimize.anneal import anneal



MaxValue = 1e36

class Anneal (multi.ModelLC):

	def __init__ (self, nl, pl, desc=misc.default):
	
		self.ma = multi.ModelLC ()
		
		self.vl  = pl[0]
		self.F   = pl[2]		
		
		fl = pl[1]	
				
		self.schedule = pl[3]
		
		self.feps = pl[4]
		self.maxeval = pl[5]

		self.A = pl[6]
		self.p = pl[7]
		
		self.dwell = pl[8]
		self.T0 = pl[9]
		self.Tf = pl[10]
		self.maxaccept = pl[11]
		
		self.maxiter = pl[12]
		self.learn_rate = pl[13]
		self.boltzmann = pl[14]
		
		self.quench = pl[15]
		self.m = pl[16]
		self.n = pl[17]
		

		if desc != misc.default:
			self.ma.SetScheme(desc)
			self.ma.SetDescription('Anneal optimization: '+desc)

	
		fl = misc.Expand (fl)
		for i in fl:
			self.ma.AddLoadcase (i.lc)
		
		self.vl = misc.Expand(self.vl)
		self.vl0 = []
		self.upper = []
		self.lower = []
		self.bounds = []
		for i in self.vl:
			self.ma.AddParameter (i.Name)
			self.ma.AddExtParameter (i.Name)
			self.vl0.append (i.Value0)
			
			if (i.Max == None):
				self.upper.append ((MaxValue))
			else:
				self.upper.append ((i.Max))
			if (i.Min == None):
				self.lower.append ((-MaxValue))
			else:
				self.lower.append ((i.Min))
				
			self.bounds.append ((i.Min, i.Max))
			
		self.ma.AddExtParameter ('Objective')
		
		self.Run()
		misc.SetSolver ("")
		misc.SetPost(os.getenv("DINSYS")+"\dinama\post\Postprocessor")
		
		misc.SetPostFile(self.ma.GetHistoryFile())
						
	def Run (self):
				
		self.iteration = 0
		self.ma.initHistory()
		
#		print 'point1: ', self.upper, self.lower
		
		(self.xopt, r) = anneal (self.Objective, self.vl0, schedule = self.schedule, T0=self.T0, 
														Tf=self.Tf, maxeval=self.maxeval, maxaccept=self.maxaccept, maxiter=self.maxiter,
														learn_rate=self.learn_rate, boltzmann=self.boltzmann, feps=self.feps,quench=self.quench,
														m=self.m, n=self.n, lower=self.lower, upper=self.upper, dwell=self.dwell)

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
			return Anneal.MaxValue
		
			
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