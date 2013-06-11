# -*- coding: cp1251 -*-


#import constants as constants
import misc

class Grain:
	def __init__ (self):
		self.atoms = []
		self.Color = 'LIMEGREEN'
		self.radius = 0.1
		self.name = ''

class Crystal :# (ParameterValues):

	def __init__ (self, nl, pl, desc=misc.default):
		
		self.Name = pl[0] 
		self.Type = pl[1]
		self.Values = pl[2]
		self.sizes = pl[3]
		self.OLSK = pl[4]
		self.radius = pl[5]
		self.Color = pl[6]

		
		self.crystal = self.generate()
		
#		solver = Solver.getSolver()
#		solver.addObject (self)
		
	def generate (self):
		
#		print self.Type
		if  self.Type=='Кубическая_примитивная':
			grain = self.cube_simple ()
		elif  self.Type=='Кубическая_гранецентрированная':
			grain = self.cube_face ()
		elif  self.Type=='Тетрагональная_объемноцентрическая':
			grain = self.tetra_volume(self.Values [0], self.Values [1],self.Values [2])
		elif  self.Type=='Тетрагональная_примитивная':
			grain = self.tetra_simple (self.Values [0], self.Values [1],self.Values [2])
		else:
			print 'Error: unknown type of grain'
		
		grain.name = self.Name
		
		return grain
		
	def cube_simple (self):
		
		grain = Grain ()
		a = self.Values [0]
		
		grain.Color = self.Color
		grain.radius = self.radius
		
		for i in xrange (self.sizes[0]):
			xc = self.OLSK[0] + i * a
			for j in xrange (self.sizes[1]):
				yc = self.OLSK[1] + j * a
				for k in xrange (self.sizes[2]):
					zc = self.OLSK[2] + k * a
					grain.atoms.append ((xc,yc,zc))
		
		return grain

	def cube_face (self):
		
		grain = self.cube_simple()
#		grain = Grain ()
#		grain.Color = self.Color
#		grain.radius = self.radius

		a = self.Values [0]
		
		for i in xrange (self.sizes[0]-1):
			xc = self.OLSK[0] + i * a + a/2.0
			
			for j in xrange (self.sizes[1]): # цикл по yz
				yc = self.OLSK[1] + j * a #+ a/2.0
				for k in xrange (self.sizes[2]-1): # цикл по xz
					zc = self.OLSK[2] + k * a + a/2.0
					grain.atoms.append ((xc,yc,zc))

			for j in xrange (self.sizes[1]-1): # цикл по yz
				yc = self.OLSK[1] + j * a + a/2.0
				for k in xrange (self.sizes[2]): # цикл по xz
					zc = self.OLSK[2] + k * a
					grain.atoms.append ((xc,yc,zc))

		for i in xrange (self.sizes[0]):
			xc = self.OLSK[0] + i * a 
			
			for j in xrange (self.sizes[1]-1): # цикл по yz
				yc = self.OLSK[1] + j * a + a/2.0
				for k in xrange (self.sizes[2]-1): # цикл по xz
					zc = self.OLSK[2] + k * a + a/2.0
					grain.atoms.append ((xc,yc,zc))

		return grain
		
	def tetra_volume (self, a, b, c):
		
		grain = self.tetra_simple(a,b,c)
		
		for i in xrange (self.sizes[0]-1):
			xc = self.OLSK[0] + i * a + a/2.0
			
			for j in xrange (self.sizes[1]-1): # цикл по yz
				yc = self.OLSK[1] + j * b + b/2.0
				for k in xrange (self.sizes[2]-1): # цикл по xz
					zc = self.OLSK[2] + k * c + c/2.0
					grain.atoms.append ((xc,yc,zc))

		return grain

	def tetra_simple (self, a, b, c):
		
		grain = Grain ()
		grain.Color = self.Color
		grain.radius = self.radius
		
		for i in xrange (self.sizes[0]):
			xc = self.OLSK[0] + i * a
			for j in xrange (self.sizes[1]):
				yc = self.OLSK[1] + j * b
				for k in xrange (self.sizes[2]):
					zc = self.OLSK[2] + k * c
					grain.atoms.append ((xc,yc,zc))
		
		return grain
		
				
				
				