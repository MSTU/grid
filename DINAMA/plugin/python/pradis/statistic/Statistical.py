# -*- coding: cp1251 -*-
import multi
import af
import glb
import misc
import os
import math

#import scipy

#from numpy import copy



MaxValue = 1e36

class Statistical (multi.ModelLC):

	def __init__ (self, nl, pl, desc=misc.default):

		self.ma = multi.ModelLC ()

		self.samples = pl[0]
		self.names  = pl[1]
		self.method = pl[2]
		
		if desc != misc.default:
			self.ma.SetScheme(desc)
			self.ma.SetDescription('Statistical: '+desc)

	
#		fl = misc.Expand (fl)
		
		
		for i in self.names:
			self.ma.AddParameter (str(i)+'.Mean')
			self.ma.AddExtParameter (str(i)+'.Mean')
		
#		self.createNormX()		
		
		
		self.Run()
		misc.SetSolver ("")
		misc.SetPost(os.getenv("DINSYS")+"\dinama\post\Postprocessor")
		
		misc.SetPostFile(self.ma.GetHistoryFile())
					
				
	def Run (self):
				
		self.ma.SetFilePostfix ('.stat')
		self.ma.initHistory()

		
		if self.method == 'point':
			j = 0
			for i in self.samples:
				y  = 777 #mean (i)
# mean calculation y=mean(x)	
				print 'y=',y
				self.ma.SetParameterValue (j, str(y))
				self.ma.SetExtParameterValue (j, str(y))
				j = j+1
			
			self.ma.writeHistory(0)
		else:
			nlayers = len(self.samples[0])
			
# создать список list из nlayers пустых элементов			
			
			for k in xrange (nlayers):
				j = 0
				for i in self.samples:
					y  = 777 #mean (i[0:k])
# mean calculation y=mean(x)	
					self.ma.SetParameterValue (j, str(y))
					self.ma.SetExtParameterValue (j, str(y))
					j = j+1
				self.ma.writeHistory(k)
				
		
