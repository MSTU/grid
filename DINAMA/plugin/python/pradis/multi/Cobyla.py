from __future__ import nested_scopes

import multi
import af
import glb
import misc
import os
import math



#from scipy.optimize.fmin_cobyla import fmin_cobyla
#from _cobyla.fmin_cobyla import fmin_cobyla
#	import _cobyla
import scipy.optimize._cobyla
from numpy import copy



MaxValue = 1e36

class Cobyla (multi.ModelLC):

	def __init__ (self, nl, pl, desc=misc.default):

		self.ma = multi.ModelLC ()

		self.vl  = pl[0]
		self.F   = pl[2]		
		
		fl = pl[1]	
		self.fce = pl[3]					
		self.rhobeg = pl [4]
		self.rhoend = pl[5]
		self.maxfun = pl[6]
					

		if desc != misc.default:
			self.ma.SetScheme(desc)
			self.ma.SetDescription('Cobyla optimization 2: '+desc)

	
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
			
			
		
			
		self.ma.AddExtParameter ('Objective')
		self.ce = self.CreateBounds(self.vl, self.fce)
		
		self.Run()
		misc.SetSolver ("")
		misc.SetPost(os.getenv("DINSYS")+"\dinama\post\Postprocessor")
		
		misc.SetPostFile(self.ma.GetHistoryFile())
						
	def Run (self):
				
		self.iteration = 0
		self.ma.initHistory()
		
		self.xopt = self.fmin_cobyla (self.Objective, self.vl0, self.ce, rhobeg=self.rhobeg, rhoend=self.rhoend, maxfun=self.maxfun)
		
		
		
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
			return Cobyla.MaxValue
		
		value = self.F (x, self.ma)		
				
		self.ma.SetExtParameterValue (len, str(value))
		
		
		return value
		
	def Constraints (self, x, c, j):
		
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
				fmin = lambda x, y=i, n=j: -x[n] + y.Min
			if i.Max != None:
				fmax = lambda x, y=i, n=j: -y.Max + x[n] 
			
			if fmin!=None:
				lce.append (fmin)
			if fmax!=None:
				lce.append (fmax)


			j=j+1
		
		num =len(vl) + 1
		for i in ce:
			f = lambda x, c = i, j = num, obj = self: obj.Constraints (x, c, j)
			lce.append (f)
			self.ma.AddExtParameter ('Constraint.'+str(i.__name__ ))
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
			
			
			f = func(x, *args)
			k = 0
			for constraints in cons:
				con[k] = constraints(x, *consargs)
				k += 1
			
			
			
			self.ma.writeHistory(self.iteration)
			
			return f
	
		xopt = scipy.optimize._cobyla.minimize(calcfc, m=m, x=copy(x0), rhobeg=rhobeg, rhoend=rhoend,
							iprint=iprint, maxfun=maxfun)
		
		return xopt
