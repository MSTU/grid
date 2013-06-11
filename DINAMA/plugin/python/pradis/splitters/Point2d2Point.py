import af
import misc
from glb import *
from Node import *
#from DOF import *
from DOF1 import *
from Point import *
from Point2d import *
import pradis.splitters.Point2d2DOFs
from Model import *

class Point2d2Point:

  def  cross(self, x,y):
    a = x[1]*y[2]-y[1]*x[2]
    b = - (x[0]*y[2]-y[0]*x[2])
    c = x[0]*y[1]-x[1]*y[0] 
    return [a,b,c]
  
  def  norm(self, x):
    L =  math.sqrt (x[0]*x[0]+x[1]*x[1]+x[2]*x[2])
#    L = L * 1e6
    return [x[0]/L, x[1]/L, x[2]/L]

  def  mul(self, x, k):
    
    return [x[0]*k, x[1]*k, x[2]*k]

  
  def diff(self, x,y):
#    print x
#    print y
    a = x[0]-y[0]
    b = x[1]-y[1]
    c = x[2]-y[2]
    return [a,b,c]
  
  def add(self, x,y):
    a = x[0]+y[0]
    b = x[1]+y[1]
    c = x[2]+y[2]
    return [a,b,c]

  def __init__(self, nl, pl, desc = misc.default):
    pl = misc.unpackDataFromList(pl)
    pl = misc.Expand(pl)
    
#    print 'pl=',pl
    
    or_ = pl[0:3]
    x =  pl[3:6]
    y =  pl[6:9]
    kx = pl[9]
    ky = pl[10]
    kt = pl[11]
    
  
    vx = self.diff (x,or_)
    vy = self.diff (y,or_)
  
    vy = self.norm (vy)
    vx = self.norm (vx)

    vz = self.cross (vx,vy)
    vy = self.cross (vz, vx)
    
  
    vx = self.norm (vx)
    vy = self.norm (vy)
    vz = self.norm (vz)
    x = self.add (or_, self.mul(vx,-1))
    pointY = self.add (or_, self.mul(vy,-1))
    pointZ = self.add (or_, self.mul(vz,-1))
  
    _net0 = nl[0]
    _net1 = DOF1()
    _net2 = DOF1()
    _net3 = DOF1()
    _net4 = nl[1]
    SX131 = Model('SX13',[_net2,_net4],[pointY,or_, ky, 0.0], desc = misc.ppl_scheme_desc(desc,'SX131') )
    SR131 = Model('SR13',[_net3,_net4],[pointZ,or_, kt], desc = misc.ppl_scheme_desc(desc,'SR131') )
    SX132 = Model('SX13',[_net1,_net4],[x,or_, kx, 0.0], desc = misc.ppl_scheme_desc(desc,'SX132') )

#    SX131 = Model('SX13',[_net2,_net4],[or_, pointY,ky, 0.0], desc = misc.ppl_scheme_desc(desc,'SX131') )
#    SR131 = Model('SR13',[_net3,_net4],[or_, pointZ,kt], desc = misc.ppl_scheme_desc(desc,'SR131') )
#    SX132 = Model('SX13',[_net1,_net4],[or_, x,kx, 0.0], desc = misc.ppl_scheme_desc(desc,'SX132') )
		
    Point2d2DOFs1 = pradis.splitters.Point2d2DOFs.Point2d2DOFs([_net0,_net1,_net2,_net3], [], desc = desc )		


