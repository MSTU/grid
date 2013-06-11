import multi
import af
import glb
import misc
import os
import math

#import scipy

from numpy import copy



MaxValue = 1e36

class Sensitivity (multi.ModelLC):

	def __init__ (self, nl, pl, desc=misc.default):

		self.ma = multi.ModelLC ()

		self.method = pl[0]
		
		self.vl  = pl[1]
		fl = pl[2]	
		self.fce = pl[3]					
			
				
		self.dx = pl [4]

		
		if desc != misc.default:
			self.ma.SetScheme(desc)
			self.ma.SetDescription('Sensitivity: '+desc)

	
		fl = misc.Expand (fl)
		for i in fl:
			self.ma.AddLoadcase (i.lc)
		
		self.vl = misc.Expand(self.vl)
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
		

#		vl0 = self.NormX (self.vl0)
#		print 'vl0=',self.vl0

		if self.method == 'Forward':
			self.forwback (1.0)
			return
		
		elif self.method == 'Backword':
			self.forwback (-1.0)

		else:
			print
			print 'Sensitivity Error: method ', self.method, 'is absent'
			print
			return
#		print 'point2'
		
		self.Objective(self.xopt)	

	def forwback (self, k):

		self.ma.SetFilePostfix ('_sen')
		self.iteration = 1
		j = 0
		x = self.vl0
#		print 'point3:', x, 'vl0=', self.vl0, 'x_=', x_
		
		for i in x:
			self.ma.SetParameterValue (j, str(i))
			self.ma.SetExtParameterValue (j, str(i))
			j = j+1
		len = j

# first analysis

		c = self.ma.Run()
		if c != 0:
			print 'Sensitivity: Error code = ', c
		
		self.Criteria (x)
		
		self.ma.writeHistory(self.iteration)


# other analyses
		for ii in range (0,len):
			self.iteration = self.iteration + 1
			x = []
			for i in self.vl0:
				x.append(i)
			(xa, xb) = self.bounds[ii]
			x [ii] = x [ii] + k*self.dx*(xb-xa)
			j = 0
			for i in x:
				self.ma.SetParameterValue (j, str(i))
				self.ma.SetExtParameterValue (j, str(i))
				j = j+1
			
			c = self.ma.Run()
			if c != 0:
				print 'Sensitivity: Error code = ', c
			
			self.Criteria (x)
			self.ma.writeHistory(self.iteration)
		

	
	def Criteria (self, x ):
		j = len(self.vl0) 
		ii = 0


		for constraints in self.fce:
			r = constraints (x, self.ma)
			self.ma.SetExtParameterValue (j, str(r))
			
			self.fvalue.append (r);
			j+=1
			ii+=1
			
#			print self.fvalue

#		print 'debug:criteria.1'

#		j = len(self.vl0) + len (self.fce)+1
		ii = 0
		for constraints in self.fce:
			if (self.iteration==1):
				self.ma.SetExtParameterValue (j, '0.0')
			else:
				(xa, xb) = self.bounds[self.iteration-2]
				dx = self.dx*(xb-xa)
				fx = (self.fvalue[len (self.fce)*(self.iteration-1)+ii]-self.fvalue[ii])/dx
				
#				print 'ii=',len (self.fce)*(self.iteration-1)+ii,' jj=',ii
					
				self.ma.SetExtParameterValue (j, str(fx))
			ii += 1
			j  += 1
			
				 
			
			

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

	def NormBoundsAnneal (self, x):
		j = 0
		ymin = []
		ymax = []
		for i in x:
			(min, max) = i
			if min != None:
				min = min / self.normX [j]
			else:
				min = -MaxValue
			if max != None:
				max = max / self.normX [j]
			else:
				max = MaxValue
			
			ymin.append ((min))
			ymax.append (max)
			j +=1
			
		return (min, max)
		
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
		for i in self.fce:
			self.ma.AddExtParameter ('Sensitivity.'+str(i.__name__ ))

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
