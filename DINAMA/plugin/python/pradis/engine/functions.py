from math import *
from numpy import *
from scipy import *

def printObject(object):
    print object

def signum(a):
    if a >= 0:
        return 1
    else:
        return -1

def getVectorLen(pointA = [0,0,0], pointB = [0,0,0]):
    p1 = array(pointA)
    p2 = array(pointB)
    if (len(p1) == len(p2)):
        num = len(p1)
        sum = float(0)
        i = float(0)
        while i < num:
            sum += (float(p2[i] - p1[i]))**2
            i += 1
        return float(math.sqrt(sum))
    else:
        return 0

def getTransformationMatrix(pointM = [0,0,0], pointN = [0,1,0], pointZ = [0,0,1]):
    pM = array(pointM)
    pN = array(pointN)
    pZ = array(pointZ)
    
    if (len(pM) == len(pN) == len(pZ)):
        num = len(pM)
        i = float(0)
        len_MN = float(0)
        len_MZ = float(0)
        cos_ = float(0)
        e1 = zeros(3)
        e2 = zeros(3)
        e3 = zeros(3)
        while i < num:
            e1[i] = float(float(pN[i] - pM[i]))
            e3[i] = float(float(pZ[i] - pM[i]))
            i += 1
        len_MN = getVectorLen(pointM,pointN)
        len_MZ = getVectorLen(pointM,pointZ)
        if len_MN == float(0):
            len_MN = float(1)
        if len_MZ == float(0):
            len_MZ = float(1)            
        e1 = array(e1) / len_MN
        e3 = array(e3) / len_MZ
        e2 = cross(e3,e1)
        e2 = (e2) / getVectorLen([0.,0.,0.],e2)
        e3 = cross(e1,e2)
        
        T = array([e1,e2,e3])
        return T
#        .transpose()
    else:
        return -1

def getPoint(pointA = [0,0,0], T = zeros((3,3)), P=[0,0,0]):
    p = asmatrix(array(pointA)) * T + asmatrix(array(P))
    return p.tolist()[0]
#    .tolist()

def getPoint2(pointA = [0,0,0], T = zeros((3,3)), P=[0,0,0]):
    p = asmatrix(array(pointA)) * T + asmatrix(array(P))
    
    print '1:', array(pointA)
    print '2:', array(P)
    print '3:', T
    print '4:', asmatrix(array(pointA))
    
    return p.tolist()

         
def getMaxShift(profile = [0,0,0], dim = 2):
    p = array(profile)
    num = len(p)
    i = 1
    maximum = 0
    if (num > dim):
        maximum = p[dim - 1]
        while i < num:
            if (p[i] > maximum):
                maximum = p[i]
            i += dim
        return maximum
    else:
        return 0.0

def getMinShift(profile = [0,0,0], dim = 2):
    p = array(profile)
    num = len(p)
    i = 1
    maximum = 0
    if (num > dim):
        maximum = p[dim - 1]
        while i < num:
            if (p[i] < maximum):
                maximum = p[i]
            i += dim
        return maximum
    else:
        return 0.0        
        
def getPoint_32(pointA = [0,0,0]):
    p = zeros(2)
    p[0] = pointA[0]
    p[1] = pointA[1]
    return p.tolist()
    
def middlePoint (p1, p2):
    pM = array(p1)
    pN = array(p2)
    return (pM + pN)/2.0
    
def pointXfromYZ (origin, pointY, pointZ):
    pM = array(origin)
    pN = array(pointY)
    pZ = array(pointZ)
    e1 = zeros(3)
    e2 = zeros(3)
    e3 = zeros(3)
    i = 0
    num = len(pM)
    while i < num:
        e2[i] = float(float(pN[i] - pM[i]))
        e3[i] = float(float(pZ[i] - pM[i]))
        i += 1

    e1 = cross(e2,e3)
    pX = pM + e1
    
    return pX.tolist()