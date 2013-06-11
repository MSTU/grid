import af
import misc
from glb import *
from Node import *
#from DOF import *
from DOF1 import *
from Point import *
from Point2d import *
from XYZ import *
import pradis.splitters.Point2XYZs
from Model import *

class PRLink2:

	def __init__(self, nl, pl, desc = misc.default):
		pl = misc.unpackDataFromList(pl)
		pl = misc.Expand(pl)

		import pradis.splitters.Point2XYZs
		pA = pl[0:3]
		pB = pl[3:6]
		pM = pl[6:9]
		pZ  = pl[9:12]
		pX  = pl[12:15]
		G = 1.0/pl [15]
		T = G/1.0
		M = pl[16]
		Jx= pl[17]
		Jy= pl[18]
		Jz= pl[19]
		Shape = pl[20:]
		
		h1 = math.sqrt( (pM[0]-pB[0])**2  + (pM[1]-pB[1])**2+(pM[2]-pB[2])**2)/20.0
		h2 = math.sqrt( (pM[0]-pA[0])**2  + (pM[1]-pA[1])**2+(pM[2]-pA[2])**2)/20.0
		h = (h1+h2)/2.0
		
		_net0 = Point()
		_net1 = Point()
		_net2 = Point()
		_net3 = XYZ()
		_net4 = XYZ()
		_net5 = XYZ()
		_net6 = XYZ()
		_net2 = nl [1]
		_net1 = nl [0]
		MJ3D1 = Model('Masses.MJ3D',[_net0],[pM, pZ, pX, M, Jx,Jy,Jz], desc = misc.ppl_scheme_desc(desc,'MJ3D1') )
		SV3DK2 = Model('Links.SV3DK',[_net2,_net0],[pB, pM, pX, G, G, T, G], desc = misc.ppl_scheme_desc(desc,'SV3DK2') )
		SV3DK1 = Model('Links.SV3DK',[_net0,_net1],[pM, pA, pX, G, G, T, G], desc = misc.ppl_scheme_desc(desc,'SV3DK1') )
#		MJ3D1_image = misc.AddImage('Images.ELP3D', MJ3D1, [ pM,  pA,  pX,  h,h,h,    5,    5],['yellow', 'Plastic', 0.0], desc = misc.ppl_scheme_desc(desc,'Mass') )
		if (Shape[0] == 0):
			MJ3D1_image = misc.AddImage('Images.EL3DP', MJ3D1, [ pM,  pM,   pZ,  pX,  h,h,h,   2,   5,   5],['yellow', 'Plastic', 0.0], desc = misc.ppl_scheme_desc(desc,'Mass') )
		elif Shape[0]<0:
			pass
		else:
			MJ3D1_image = misc.AddImage('Geometry.SHAPE', MJ3D1, [ pM,  pM, pZ,  pX,  Shape,  0],['yellow', 'Plastic', 0.0], desc = misc.ppl_scheme_desc(desc,'Mass') )
		Point2XYZs2 = pradis.splitters.Point2XYZs.Point2XYZs([_net0,_net3,_net4], [], desc = misc.ppl_scheme_desc(desc,'Point2XYZs2') )
		Point2XYZs3 = pradis.splitters.Point2XYZs.Point2XYZs([_net2,_net5,_net4], [], desc = misc.ppl_scheme_desc(desc,'Point2XYZs3') )
		Point2XYZs1 = pradis.splitters.Point2XYZs.Point2XYZs([_net1,_net6,_net4], [], desc = misc.ppl_scheme_desc(desc,'Point2XYZs1') )

