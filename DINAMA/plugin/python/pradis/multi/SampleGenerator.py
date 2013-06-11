import multi
import af
import glb
import misc
import os
import math
#import random


#import scipy

from numpy import copy



MaxValue = 1e36

class SampleGenerator (multi.ModelLC):

	def __init__ (self, nl, pl, desc=misc.default):

		self.ma = multi.ModelLC ()

		self.method = pl[0]		# generator method
		
		self.vl  = pl[1]		# variables list
		self.vl_low  = pl[2]	# variable low list
		fl = pl[3]				# loadcases list
		self.fce = pl[4]		# criteria list
		self.count = pl [5]		# experiments count
				

		
		if desc != misc.default:
			self.ma.SetScheme(desc)
			self.ma.SetDescription('SampleGenerator: '+desc)

	
		fl = misc.Expand (fl)
		for i in fl:
			self.ma.AddLoadcase (i.lc)	
		
#		print 'vl2=', self.vl
		self.vl = misc.Expand(self.vl)
		
		
		
		self.vl_low = misc.Expand(self.vl_low)
		self.fce = misc.Expand(self.fce)
		
		
		self.fvalue = []
		self.vl0 = []
		self.bounds = []
		for i in self.vl:
			self.ma.AddParameter (i.Name)
			self.ma.AddExtParameter (i.Name)
			self.vl0.append (i.Value0)
			self.bounds.append ((i.Min, i.Max))
		
#		self.createNormX()		
		
		self.addCriteryHistory()
		
		self.Run()
		misc.SetSolver ("")
		misc.SetPost(os.getenv("DINSYS")+"\dinama\post\Postprocessor")
		
		misc.SetPostFile(self.ma.GetHistoryFile())
					
				
	def Run (self):
				
		self.iteration = 0
		self.ma.initHistory()
		self.generate ()

#		vl0 = self.NormX (self.vl0)
#		print 'vl0=',self.vl0

#		print 'point2'
		
#		self.Objective(self.xopt)	

	def sample_generator (self,n_exp):
		if self.method == 'Stochastic':
			return self.stochastic (n_exp)
			
		
		elif self.method == 'Scanner':
			return self.scanner (n_exp)

		else:
			print
			print 'SampleGenerator Error: method ', self.method, 'is absent'
			print
			return None

	def stochastic(self,n_exp):
		x = []
		i = 0
		for v in self.vl:
			low = self.vl_low[i]
			
#			print '############333'
#			print 'v = ',v 
#			print 'v0 = ',v.Value0
#			print 'low = ', low
			if (low):
				value = low.low (v)
			else:
				value = self.v.Value0
			
#			print 'value = ', value
			x.append(value)
			i+=1
		
		print 'x=',x
		return x

	def scanner(self,n_exp):
		x = []
		i = 0
		for v in self.bounds:
			(min,max) = v
			value = min + (max-min)*n_exp/float (self.count)
			
			x.append(value)
			i+=1
		return x
		
		
	def generate (self):

		self.ma.SetFilePostfix ('.sample')
		
		for n_exp in range (self.count): # cycle for experiments
		
			self.iteration = n_exp
		# here you must call the generator like that
			x = self.sample_generator (n_exp)
		# ######
#			print 'x=',x
		
#		print 'point3:', x, 'vl0=', self.vl0, 'x_=', x_
		
			j = 0
			# set values for history file
			for i in x:
				self.ma.SetParameterValue (j, str(i))
				self.ma.SetExtParameterValue (j, str(i))
				j = j+1
			len = j


			# run analysis
			c = self.ma.Run()
			if c != 0:
				print 'SampleGenerator: Error code = ', c
		
			# criteria analysis
			self.Criteria (x)
			self.ma.writeHistory(self.iteration)

			
			
	
	def Criteria (self, x ):
		j = len(self.vl0) 
		ii = 0


		for constraints in self.fce:
			r = constraints (x, self.ma)
			self.ma.SetExtParameterValue (j, str(r))
			
			j+=1
			

	def createNormX(self):
		j = 0
		self.normX = []
		for i in self.vl0:
			(min,max) =self.bounds [j]
			
			norm = math.fabs (self.vl0[j])
			if (min!=None):
				norm = norm + math.fabs (min)
			if (max!=None):
				norm = norm + math.fabs (max)
			norm = norm / 3.0
			if norm == 0.0:
				norm = 1.0	
			
			self.normX.append (norm)
			
			j = j + 1
		
	def NormX (self, x):
		j = 0
		y = []
		for i in x:
#			print i,' ', self.normX [j]
			a = i / self.normX [j]
#			print 'a=',a
			y.append (a)
			j +=1
		return y

	def NormBounds (self, x):
		j = 0
		y = []
		for i in x:
			(min, max) = i
			if min != None:
				min = min / self.normX [j]
			if max != None:
				max = max / self.normX [j]
			j +=1
			y.append ((min, max))

		
	def aNormX(self, x):
		j = 0
		y = []

#DOIT:
#		print 'DEBUG: x = ',x
		if x ==None:
			return 0
		for i in x:
			y.append (i*self.normX [j])
			j +=1
		
		return y
		
		

	def addCriteryHistory(self):
		for thisfunc in self.fce:
			if not callable(thisfunc):
				print 'point_func: ', str (thisfunc)
				raise TypeError(err)
		for i in self.fce:
			self.ma.AddExtParameter (str(i.__name__ ))

#			
# Methods for Cobyla
#
#			
	def Constraints (self, x_, c, j):
		
		x = self.aNormX(x_)
		r = c (x, self.ma)
		self.ma.SetExtParameterValue (j, str(r))
		
		return r
	
	def CreateBounds (self, vl, ce): 
		lce = []
		j = 0
#		print 'Bounds:'
#		print
#		print
		
		for i in vl:
			fmin = None
			fmax = None
			
			if i.Min != None:
				a = i.Min / self.normX [j]
				fmin = lambda x, y=a, n=j: x[n] - y
			if i.Max != None:
				a = i.Max / self.normX [j]
				fmax = lambda x, y=a, n=j:  y - x[n] 
			
			if fmin!=None:
				lce.append (fmin)
			if fmax!=None:
				lce.append (fmax)


			j=j+1
		
		num =len(vl) + 1
		for i in ce:
			f = lambda x, c = i, j = num, obj = self: - obj.Constraints (x, c, j)
			lce.append (f)
			num=num+1
		
		return lce
