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
from scipy.optimize.lbfgsb import fmin_l_bfgs_b
from scipy.optimize.tnc import fmin_tnc
from scipy.optimize.anneal import anneal
import scipy.optimize._cobyla
from numpy import copy
from scipy.optimize import golden
from scipy.optimize import brent
from scipy.optimize import bracket
from scipy.optimize import fminbound



MaxValue = 1e36

class Optimization (multi.ModelLC):

	def __init__ (self, nl, pl, desc=misc.default):

		self.ma = multi.ModelLC ()

		self.method = pl[0]
		
		self.vl  = pl[1]
		fl = pl[2]	
		self.F   = pl[3]		
		self.fce = pl[4]					
#		self.target = pl[5]
#		self.constraitmethod = pl[6]
			
				
		self.xtol = pl [5]
		self.ftol = pl[6]
		self.maxfun = pl[7]
		self.A = pl[8]
		self.p = pl[9]
					
		self.epsilon = 1e-4
		self.schedule = 'fast'
		self.isCobyla = None
		self.rhobeg = 1.0
		self.rhoend = 1e-4
		
		if desc != misc.default:
			self.ma.SetScheme(desc)
			self.ma.SetDescription('Optimization: '+desc)

	
		fl = misc.Expand (fl)
		for i in fl:
			self.ma.AddLoadcase (i.lc)
		
		self.vl = misc.Expand(self.vl)
		self.fce = misc.Expand(self.fce)
		
		
		
		self.vl0 = []
		self.bounds = []
		for i in self.vl:
			self.ma.AddParameter (i.Name)
			self.ma.AddExtParameter (i.Name)
			self.vl0.append (i.Value0)
			self.bounds.append ((i.Min, i.Max))
		
		self.createNormX()		
		
		self.ma.AddExtParameter ('Objective')
		self.addCriteryHistory()
		
		self.Run()
		misc.SetSolver ("")
		misc.SetPost(os.getenv("DINSYS")+"\dinama\post\Postprocessor")
		
		misc.SetPostFile(self.ma.GetHistoryFile())
					
				
	def Run (self):
				
		self.iteration = 0
		self.ma.initHistory()
		
#		print 'point1'

		vl0 = self.NormX (self.vl0)
#		print 'vl0=',self.vl0

		if self.method == 'Opt_1D':
			(xa, xb) = self.bounds[0]
#			print 'xa=',xa,' xb=',xb
			xa = self.NormX ([xa])
			xb = self.NormX ([xb])
			self.xopt = fminbound (self.Objective1D, xa[0], xb[0], xtol = self.xtol, maxfun = self.maxfun)
			self.Objective1D(self.xopt)	
			return

		
		elif self.method == 'NelderMead':
			self.xopt = fmin (self.Objective, vl0, xtol=self.xtol, ftol=self.ftol, maxfun=self.maxfun)
		elif self.method == 'Powell':
			self.xopt = fmin_powell (self.Objective, vl0, xtol=self.xtol, ftol=self.ftol, maxfun=self.maxfun)
		elif self.method == 'LBFGSB':
			bounds = self.NormBounds (self.bounds)
			(self.xopt, f, d) = fmin_l_bfgs_b (self.Objective, vl0, approx_grad=1, bounds = bounds, epsilon=self.epsilon, maxfun=self.maxfun)
		elif self.method == 'TNC':
			bounds = self.NormBounds (self.bounds)
			(self.xopt, f, d) = fmin_tnc (self.Objective, vl0, approx_grad=1, bounds = bounds, ftol=self.ftol, xtol=self.xtol, epsilon=self.epsilon, maxfun=self.maxfun)
		elif self.method == 'Anneal':
			(lower, upper) = self.NormBoundsAnneal(self.bounds)
			(self.xopt, r) = anneal (self.Objective, vl0, schedule = self.schedule, 
														maxeval=self.maxfun, feps=self.ftol, lower=lower, upper=upper)
		elif self.method == 'Cobyla':
			self.isCobyla = 1
			self.ce = self.CreateBounds(self.vl, self.fce)
			self.xopt = self.fmin_cobyla (self.Objective, vl0, self.ce, rhobeg=self.rhobeg, rhoend=self.rhoend, maxfun=self.maxfun)

		else:
			print
			print 'Optimization Error: method ', self.method, 'is absent'
			print
			return
#		print 'point2'
		
		self.Objective(self.xopt)	

	def Objective1D (self, x):
		
#		print 'x=',x
		x_ = [x]
		value = self.Objective (x_)
		return value	

	
	def Objective (self, x_):
		self.ma.SetFilePostfix ('_opt')
		self.iteration = self.iteration + 1
		j = 0
		x = self.aNormX(x_)
#		print 'point3:', x, 'vl0=', self.vl0, 'x_=', x_
		
		for i in x:
			self.ma.SetParameterValue (j, str(i))
			self.ma.SetExtParameterValue (j, str(i))
			j = j+1
		len = j

		c = self.ma.Run()
		if c != 0:
			print 'Optimization: Error code = ', c
			return Optimization.MaxValue
		
		value = self.F (x, self.ma)		
		penc = 0.0
		if self.isCobyla!=1:
			penc = self.CriteriaPenalty (x)
		pen = self.Penalty (x, self.bounds)
		
		
		self.ma.SetExtParameterValue (len, str(value))
		if self.isCobyla!=1:
			self.ma.writeHistory(self.iteration)

		value = value		 + penc+pen
		
		return value

	def CriteriaPenalty (self, x ):
		penc = 0.0
		j = len(self.vl0) + 1
		for constraints in self.fce:
			r = constraints (x, self.ma)
			self.ma.SetExtParameterValue (j, str(r))
			if r > 0.0:
				penc = penc + self.A *( r )** self.p
			j+=1
		return penc

	def createNormX(self):
		j = 0
		self.normX = []
		self.normX0 = []
		for i in self.vl0:
			(min,max) =self.bounds [j]
			
			if (min!=None and max !=None):
				norm = max - min
				norm0 = min
			if (min==None and max !=None):
				norm = 2*(max - self.vl0[j])
				norm0 = 2*self.vl0[j]-max
			if (min!=None and max ==None):
				norm = - 2*(min - self.vl0[j])
				norm0 = min
			if (min==None and max ==None):
				if math.fabs (self.vl0[j])>1e-10:
					norm = 0.5*self.vl0[j]
					norm0 = 0.0
				else:
					norm = 1.0
					norm0 = 0.0
			
			self.normX.append (norm)
			self.normX0.append (norm0)
			
			j = j + 1
		
	def NormX (self, x):
		j = 0
		y = []
		for i in x:
#			print i,' ', self.normX [j]
			a = (i- self.normX0 [j]) / self.normX [j]
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
				min = (min - self.normX0 [j])/ self.normX [j]
			if max != None:
				max = (max - self0.normX [j])/ self.normX [j]
			j +=1
			y.append ((min, max))
		return y

	def NormBoundsAnneal (self, x):
		j = 0
		ymin = []
		ymax = []
		for i in x:
			(min, max) = i
			if min != None:
				min = (min - self.normX0 [j])/ self.normX [j]
			else:
				min = -MaxValue
			if max != None:
				max = (max - self.normX0 [j])/ self.normX [j]
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
			y.append (i*self.normX [j]+self.normX0 [j])
			j +=1
		
		return y
		
		
	def Penalty (self, x, bounds):
		
		r = 0.0
		j = 0
		for i in x:
			(min,max) =bounds [j]
			
			norm = self.normX[j]
			
			if min != None:
				if i<min:
					r = r + self.A *( (min- i)/norm )** self.p
			if max != None:
				if i>max:
					r = r + self.A * ((i - max)/norm) ** self.p
			j = j + 1
		
		return r
		
	def addCriteryHistory(self):
		for thisfunc in self.fce:
			if not callable(thisfunc):
				print 'point_func: ', str (thisfunc)
				raise TypeError(err)
		for i in self.fce:
			self.ma.AddExtParameter ('Constraint.'+str(i.__name__ ))

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
				a = (i.Min - self.normX0 [j])/ self.normX [j]
				fmin = lambda x, y=a, n=j: x[n] - y
			if i.Max != None:
				a = (i.Max - self.normX [j])/ self.normX [j]
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

	def fmin_cobyla(self,func, x0, cons, args=(), consargs=None, rhobeg=1.0, rhoend=1e-4,
									iprint=1, maxfun=1000):
		err = "cons must be a sequence of callable functions or a single"\
					" callable function."
		try:
			m = len(cons)
		except TypeError:
			if callable(cons):
				m = 1
				cons = [cons]
			else:
				raise TypeError(err)
		else:
#			print str (cons)
			for thisfunc in cons:
				if not callable(thisfunc):
					print 'point_func: ', str (thisfunc)
					raise TypeError(err)
		
		if consargs is None:
			consargs = args
		
		def calcfc(x, con):
					
#			print 'x=',x
			f = func(x, *args)
#			print 'f=',f
			k = 0
			for constraints in cons:
				con[k] = constraints(x, *consargs)
#				print 'com=', con[k]
				k += 1
						
			self.ma.writeHistory(self.iteration)
			
			return f
	
		xopt = scipy.optimize._cobyla.minimize(calcfc, m=m, x=copy(x0), rhobeg=rhobeg, rhoend=rhoend,
							iprint=iprint, maxfun=maxfun)
		
		return xopt
