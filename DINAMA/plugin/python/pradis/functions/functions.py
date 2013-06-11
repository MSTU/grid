from math import *
#from numpy import *
#from scipy import *

def printObject(object):
    print object

def offset (p, dp):
	return [p[0]+dp[0], p[1]+dp[1], p[2]+dp[2]]

def offset2d (p, dp):
	return [p[0]+dp[0], p[1]+dp[1]]
	
def signum(a):
    if a >= 0:
        return 1
    else:
        return -1

def getVectorLen(pointA = [0,0,0], pointB = [0,0,0]):
    p1 = pointA
    p2 = pointB
    if (len(p1) == len(p2)):
        num = len(p1)
        sum = float(0)
        i = 0
        while i < num:
            sum += (float(p2[i] - p1[i]))**2
            i += 1
        return float(sqrt(sum))
    else:
        return 0

def cross (a,b):
	return [a[1]*b[2] -a[2]*b[1], a[2]*b[0] -a[0]*b[2], a[0]*b[1] -a[1]*b[0]] 
		
def getTransformationMatrix(pointM = [0,0,0], pointN = [0,1,0], pointZ = [0,0,1]):
    pM = pointM
    pN = pointN
    pZ = pointZ
    
    if (len(pM) == len(pN) == len(pZ)):
        num = len(pM)
        i = 0
        len_MN = float(0)
        len_MZ = float(0)
        cos_ = float(0)
        e1 = [0.,0.,0.]
        e2 = [0.,0.,0.]
        e3 = [0.,0.,0.]
        while i < num:
            e1[i] = float(pN[i] - pM[i])
            e3[i] = float(pZ[i] - pM[i])
            i += 1
        len_MN = getVectorLen(pointM,pointN)
        len_MZ = getVectorLen(pointM,pointZ)
        if len_MN == float(0):
            len_MN = float(1)
        if len_MZ == float(0):
            len_MZ = float(1)            
        e1 = [e1[0] / len_MN, e1[1]/ len_MN  , e1[2]/ len_MN]
        e3 = [e3[0] / len_MZ, e3[1] / len_MZ, e3[2] / len_MZ]
        e2 = cross(e3,e1)
        len_e2 = getVectorLen([0.,0.,0.],e2)
        e2 = [e2[0]/len_e2, e2[1]/len_e2,e2[2]/len_e2]
        e3 = cross(e1,e2)
        
        T = [e1,e2,e3]
        return T
#        .transpose()
    else:
        return -1

def getPoint(pointA, T, P):
    p = [0,0,0]
#	print 'pointA = ', pointA

    p[0] = pointA[0]*(T[0])[0]+pointA[1]*(T[1])[0]+pointA[2]*(T[2])[0]+P[0]
    p[1] = pointA[0]*(T[0])[1]+pointA[1]*(T[1])[1]+pointA[2]*(T[2])[1]+P[1]
    p[2] = pointA[0]*(T[0])[2]+pointA[1]*(T[1])[2]+pointA[2]*(T[2])[2]+P[2]
#	asmatrix(array(pointA)) * T + asmatrix(array(P))
    return p
#    .tolist()

def pointXfromYZ (origin, pointY, pointZ):
    pM = origin
    pN = pointY
    pZ = pointZ
    e1 = [0.,0.,0.]#zeros(3)
    e2 = [0.,0.,0.]#zeros(3)
    e3 = [0.,0.,0.]#zeros(3)
    i = 0
    num = len(pM)
    while i < num:
        e2[i] = float(float(pN[i] - pM[i]))
        e3[i] = float(float(pZ[i] - pM[i]))
        i += 1

    e1 = cross(e2,e3)
    pX = [0,0,0]
    pX[0] = pM[0] + e1[0]
    pX[1] = pM[1] + e1[1]
    pX[2] = pM[2] + e1[2]
    
    return pX