# -*- coding: cp1251 -*-


#from misc import *
#import Solver
#from  pradis.ppl.constant import *
#import pradis.ppl.constants as constants
from pradis.grain.Crystal import Crystal
from pradis.grain.Crystal import Grain
from include import *
#import numpy
import math
#import constants as constants
import misc
#import cython
from pradis.functions.transformations import rotation_matrix
from numpy import dot
import time


class Rotation :# (ParameterValues):

	def __init__ (self, nl, pl, desc=misc.default):
		
#		import math
		self.Crystals = pl[0] 
		self.Point = pl[1]
		self.Axis = pl[2]
		self.Angle = pl[3]/180.0*math.pi
		self.radius = pl[4]
		self.Color = pl[5]
		self.min_max_angle = pl[6]
		self.angle_step = pl[7]
		self.desc = desc

		t1 = time.time()

		self.diagram = self.create_diagram()
#		print self.diagram

		dt1 = time.time()-t1
		print 'diagram time = ', dt1
		
		self.Crystals[0].crystal = self.rotation (self.Angle)	
		p3 = self.merge  (self.Crystals[0], self.Crystals)


		dt2 = time.time()-t1-dt1
		print 'merge time = ', dt2
		
		self.boundary = p3

		
		scene = Scene ()
		for i in self.Crystals:
			scene.add (i.crystal)
		scene.add (self.boundary)
		
		scene.draw(self.diagram, self.angle_step)

		dt3 = time.time()-t1-dt1-dt2
		print 'draw scene time = ', dt3
		
#		solver = Solver.getSolver()
#		solver.addObject (self)
		
	def create_diagram(self):
	
		print "start diagram creation..."
		(min_alpha, max_alpha) = self.min_max_angle#   math.pi/2.0/float(npoints)
#		max_alpha = math.pi/2.0#-min_alpha
		npoints = int ((max_alpha - min_alpha)/self.angle_step)

		(min_alpha, max_alpha)	= (min_alpha*math.pi/180.0, max_alpha*math.pi/180.0)
#		print npoints, min_alpha, max_alpha
		z0 = self.z_atoms (self.Crystals)
#		print 'z0=',z0
		xy = []#(0.0,0.0)]	
		
		t1 = time.time()
		t0=t1
		
		for i in xrange(npoints+1):
			alpha = min_alpha + (max_alpha - min_alpha) * float(i)/float(npoints)
#			if alpha < 1e-6:
#				xy.append ((0.0,0.0))
#				continue
#			alpha = self.Angle
			g = self.rotation (alpha)
			z = self.calculate_z (g,self.Crystals)
#			print 'z=',z
			if z == 0:
				ro = -1.0
			else:
				ro= (z0)/(z)
#			if len (xy):
#				(a,r) = xy[-1]
#				xy.append ((((alpha-1e-3)*180.0/math.pi), r))
				 
			xy.append ((alpha*180.0/math.pi, ro))
			
			t2 = time.time()
			if t2-t1>10:
				print int (t2-t0), " s, alpha = ", alpha*180.0/math.pi, " ..."
				t1 = t2
		
		
		(a0,ro0) = xy[0]
		if a0>1e-10:
			xy.insert (0, (0.0, ro0))
		print "end diagram creation."
		
		return xy
	
		
	def rotation (self, angle):
		
		c = self.Crystals[0]
		grain = c.crystal
		axis = self.Axis
		point = self.Point
		new_points = []
		for i in grain.atoms:
			(x,y,z) = i
			p = [x,y,z,1.0]
#			print self.Axis
#			print self.Angle
#			print self.Point
			R = rotation_matrix (angle, axis, point)
#			print R
#			print p

			p2 = dot (R,p)
#			print p2
			new_points.append ((p2[0], p2[1], p2[2]))
#			new_points.append ((p[0]+1, p[1]+1, p[2]+1))			
#		grain.atoms = new_points
		
#		print new_points
	
		grain2 = Grain()
		grain2.Color = c.Color
		grain2.radius = c.radius
		grain2.name = c.Name
		
		grain2.atoms = new_points
#		z1 = self.z_atoms (self.Crystals)
#		p3 = self.merge  (grain, self.Crystals)
		
#		grain2.atoms = p3
		
#		z2 = self.calculate_z ()
				
		return grain2
		
	def z_atoms (self, crystal_list):
		
		z=1e38
		for  i in crystal_list:
			if len (i.crystal.atoms) < z:
				z = len (i.crystal.atoms)
		return z

	def calculate_z (self, g, crystals):

		g3 = []
		z = 0
		g_atoms = g.atoms
		r2=self.radius*self.radius
		for i in crystals[1:]:
			g2 = i.crystal
#			g2_g = []
			for j in g2.atoms:	
				(x1,y1,z1) = j
#				g1_g = []
				for k in g_atoms:
					(x2,y2,z2) = k
					r =  ((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2)+(z1-z2)*(z1-z2))
					if r<=r2:
#						g3.append ((x1,y1,z1))
						z+=1
						break
#						del j
#						del k				
#					else:
#						g2_g.append (j)
#						g1_g.append(k)
#				g_atoms = g1_g
#			g2.atoms = g2_g
#		g.atoms = g1_g
		
		return z

		
	def merge (self, c1, crystals):
		
		g3 = []
		g= c1.crystal
		r2=self.radius*self.radius
		
		for i in crystals[1:]:    # бежим по всем кристалам кроме 1-го
			g2 = i.crystal
#			g2_g = []
			del_g2 = []
			for j in g2.atoms:		# бежим по атомам кристала
				(x1,y1,z1) = j
#				g1_g = []
				del_g = []
				for k in g.atoms:	# бежим по атомам повернутого кристала
					(x2,y2,z2) = k
					r =  ((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2)+(z1-z2)*(z1-z2))
					if r<=r2:
						g3.append ((x1,y1,z1))
						del_g2.append( i)
						del_g = k#.append(k)
						
						break
#						del j
#						del k				
#					else:
#						g2_g.append (j)
#						g1_g.append(k)
				if del_g:
					g.atoms.remove (del_g)
#				g.atoms = list(set(g.atoms).difference(del_g))
#			g2.atoms.remove (del_g2)
			g2.atoms = list(set(g2.atoms).difference(del_g2))			
#		g.atoms = g1_g
		
		
		grain3 = Grain()
		grain3.Color = self.Color
		grain3.radius = self.radius
		grain3.name = self.desc
		
		grain3.atoms = g3
		
		return grain3
						
					
			
			
			
		
class Scene:
	def __init__(self):
		self.obj_list = []
		
	def add (self, obj):
		self.obj_list.append (obj)

	def draw (self, diagram, step):
		

		import pradis.splitters.Point2d2DOFs
		_net0 = DOF1()
		_net1 = DOF1()
		_net2 = DOF1()
		gnd_base_Point2d = Point2d()
		Base ([gnd_base_Point2d])
		MD1 = Model('Masses.MD',[gnd_base_Point2d],[1.0, 1.0], desc = 'MD1' )
		

		for i in self.obj_list:
			color = i.Color
			radius = i.radius
			name = i.name
			n = 0
			for j in i.atoms:
				(xc,yc,zc) = j
				n+=1
#				print (xc,yc,zc)
#				print type(xc)
				MD1_image = AddImage('Images.POINT', MD1, [  float (xc), float (yc), float (zc),   radius,   1],[color, 'Plastic', 0.0], desc = 'p'+str(n)+'_'+name)

#  MD1_image = AddImage('Images.POINT', MD1, [  0, 0, 0,   0.2,   1],['red1', 'Plastic', 0.0], desc = misc.ppl_scheme_desc(ppl_scheme_desc,'MD1_image') )

		Point2d2DOFs1 = pradis.splitters.Point2d2DOFs.Point2d2DOFs([gnd_base_Point2d,_net0,_net1,_net2], [], desc = 'Point2d2DOFs1' )
		
		signal = []
		for i in diagram:
			(x,y) = i
			signal.append(x)
			signal.append(y)
		
		(end, v) = diagram [-1]
		(t0, v0) = diagram [0]
#		print t0,v0
		(t1, v1) = diagram [1]
		_net3 = DOF1()
		PwLinearSource1 = Model('SSIG2',[_net3],signal, desc = 'PwLinearSource1' )
		VN1 = Model('Sources.VN',[_net3],[v0], desc = 'VN1') 
		V1 = OVP('base.V',[_net3],[1.0], desc = 'Обратная плотность' )
		DISP1 = DISP([ Range (V1, -1, 1)], end = 1.0, start = 0.0, frm = 0, scale = 0, desc = 'Плотность' )

		
		smax = step/2.0
		
		Dynamic1 = Dynamic([], end = end, method = 'Stoermer', outper = 100, outvar = 1, control = smax/100.0, smax = smax/2.0, smin = 1e-11, weight = 1.0, itr = 5, drltx = 0.001, dabsx = 0.001, drltu = 0.001, dabsu = 0.001, drlti = 0.001, dabsi = 0.01, debug = 0, optim = 2, second = 0, flag = 2, checkm = 0, predict = 0, ignore = 0, out = 0, prttime = 30, save = 1e10, atm = 0, desc = 'Dynamic1' )
		
		
	
	