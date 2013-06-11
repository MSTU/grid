from s000j import *
from array import *
from numpy import *

class model:

	def __init__(COMMON, cm0,cm1,cm2,cm3,cm4,cm5,cm6,cm7,cm8,cm9,cm10, 
		cm11,cm12,cm13,cm14,cm15,cm16,cm17,cm18,cm19,cm20,
		cm21,cm22,cm23,cm24,cm25,cm26,cm27,cm28,cm29,cm30,
		cm31,cm32,cm33,cm34,cm35,cm36,cm37,cm38,cm39):


		COMMON.TIME = cm0
		COMMON.STEP = cm1
		COMMON.STEP01 = cm2
		COMMON.STEP02 = cm3
		COMMON.SMIN = cm4
		COMMON.DABSI = cm5
		COMMON.DRLTI = cm6
		COMMON.STEPMD = cm7
		COMMON.TIMEND = cm8
		COMMON.NAME = cm9
		COMMON.nLength = cm10
		COMMON.NSTEP = cm11
		COMMON.SYSPRN = cm12
		COMMON.NITER = cm13
		COMMON.ITR = cm14
		COMMON.CODE = cm15
		COMMON.NUMINT = cm16
		COMMON.NUMPP = cm17
		COMMON.CODSTP = cm18
		COMMON.CODGRF = cm19
		COMMON.NEWINT = cm20
		COMMON.MINSTP = cm21
		COMMON.RLMAX = cm22
		COMMON.RLMIN = cm23
		COMMON.MSHEPS = cm24
		COMMON.INTMAX = cm25
		COMMON.PI = cm26
		COMMON.REZB = cm27
		COMMON.REZC = cm28
		COMMON.REZD = cm29		
		COMMON.RELYX = cm30
		COMMON.XNMPXL = cm31
		COMMON.YNMPXL = cm32
		COMMON.XNMSMB = cm33
		COMMON.YNMSMB = cm34
		COMMON.NCOLOR = cm35
		COMMON.NMVPAG = cm36
		COMMON.MODES = cm37
		COMMON.IK4 = cm38
		COMMON.IS4 = cm39
	

	def Execute(COMMON, I, Y, X, V, A, PAR, NEW, OLD, WRK):
		res = return_result(COMMON, I, Y, NEW, OLD, WRK)
		return res


	
	def YakobyX (COMMON, I, Y, X, V, A, PAR,  NEW, OLD, WRK, I_function, Next, Na, eps, relativeX):
		
		#print
		#print
		#print "Yakoby. start"
		
#		eps = 1e-20
#		relativeX = 0.001
		
		#print "Yakoby. 1:", Next
		X1 = zeros (Next+1)
		#print "Yakoby. 2"
		I1 = zeros (Next+1)
		for i in xrange (1, Next+1):
			X1 [i] = X[i]
#			V1 [i] = V[i]
#			A1 [i] = A[i]
			
			
		# dX
		
		for i in xrange (1, Next+1):
			if abs(X[i]) < eps:
				dx = eps
			else:
				dx = relativeX * X[i]
			x2 = X1[i]
			X1 [i] += dx
			
			(COMMON, I1, Y, X1, V, A, NEW, OLD, WRK) = I_function (COMMON, I1, Y, X1, V, A, PAR, NEW, OLD, WRK)
			
			for j in xrange (1, Next + 1):
				Y [(j-1) * Next + i] = (I1[j] - I[j])/dx
			
			X1[i] = x2

		#print "Yakoby. end"
		
		return Y

	def YakobyV (COMMON, I, Y, X, V, A, PAR,  NEW, OLD, WRK, I_function, Next, Na, eps, relativeX):
		
		#print
		#print
		#print "Yakoby. start"
		
#		eps = 1e-20
#		relativeX = 0.001
		
		#print "Yakoby. 1:", Next
#		X1 = zeros (Next+1)
		#print "Yakoby. 2"
		V1 = zeros (Next+1)
#		A1 = zeros (Next+1)
		I1 = zeros (Next+1)
		for i in xrange (1, Next+1):
#			X1 [i] = X[i]
			V1 [i] = V[i]
#			A1 [i] = A[i]
			
			
		#print "Yakoby. 3"
		# dV
		for i in xrange (1, Next+1):
			if abs(V[i]) < eps:
				dx = eps
			else:
				dx = relativeX * V[i]
			x2 = V1[i]
			V1 [i] += dx
			
			#print "Yakoby. 3.3  dx = ", V1 [i], "  x2 = ", x2			
			
			(COMMON, I1, Y, X, V1, A, NEW, OLD, WRK) = I_function (COMMON, I1, Y, X, V1, A,PAR,  NEW, OLD, WRK)

			#print "Yakoby. 3.4  V1 [i] = ",V1 [i]			
			
			#print '=====I='
			for j in xrange (1, Next + 1):
				#print 'I[',j,'] = ', I[j], 'I1[',j,'] = ', I1[j]
				Y [(j-1) * Next + i+Na] = (I1[j] - I[j])/dx
			
			V1[i] = x2

		#print "YakobyV. end"
		
		return Y
		

	def YakobyA (COMMON, I, Y, X, V, A, PAR,  NEW, OLD, WRK, I_function, Next, Na, eps, relativeX):
		
		#print
		#print
		#print "Yakoby. start"
		
#		eps = 1e-20
#		relativeX = 0.001
		
		#print "Yakoby. 1:", Next
		A1 = zeros (Next+1)
		I1 = zeros (Next+1)
		for i in xrange (1, Next+1):
#			X1 [i] = X[i]
#			V1 [i] = V[i]
			A1 [i] = A[i]
			
			
		#print "Yakoby. 4"
		# dA
		for i in xrange (1, Next+1):
			if abs(A[i]) < eps:
				dx = eps
			else:
				dx = relativeX * A[i]
			x2 = A1[i]
			A1 [i] += dx
			
			#print "Yakoby. 4.3  dx = ", dx			
			
			(COMMON, I1, Y, X, V, A1, NEW, OLD, WRK) = I_function (COMMON, I1, Y, X, V, A1,PAR,  NEW, OLD, WRK)

			#print "Yakoby. 4.4  A1 [i] = ", A1 [i]
			
			for j in xrange (1, Next + 1):
				#print "Yakoby. 4.5   ij = ", (j-1) * Next + i +Na
				Y [(j-1) * Next + i +Na] = (I1[j] - I[j])/dx
			
			A1[i] = x2
			
			#print "YakobyA. 4.7  A1 [i] = ", I1
		#print "Yakoby. end"
		
		return Y

def printY (Y, N):
	#print 'printX.start'
	print 'model.Yv='
	
	for i in xrange (1,N+1):
		print Y[(i-1) * N+1: i*N+1]
	print 'model.Ya='
	for i in xrange (1,N+1):
		print Y[(i-1) * N+1+N**2: i*N+N**2+1]

		
	
# Turn a Python list into a C double array
def CreateDoubleArrayFromList(l):
	sj = S000J()
	d = sj.new_darray(len(l))
	for i in range(0,len(l)):
		sj.darray_set(d,i,l[i])
	return d

# Turn out an double array to Python list
def CreateListFromDoubleArray(a, length):
	sj = S000J()
	l = []
	for i in range(0,length):
		l.append(sj.darray_get(a,i))
	return l

# Turn a Python list into a C int array
def CreateIntArrayFromList(l):
	sj = S000J()
	d = sj.new_iarray(len(l))
	for i in range(0,len(l)):
		sj.iarray_set(d,i,l[i])
	return d

# Turn out an int array to Python list
def CreateListFromIntArray(a, length):
	sj = S000J()
	l = []
	for i in range(0,length):
		l.append(sj.iarray_get(a,i))
	return l


# Clear memory
def DeleteArray(a):
	sj = S000J()
	sj.delete_darray(a)



def return_result(COMMON, I, Y, X, V, A, NEW, OLD, WRK):
	comm = [COMMON.TIME, 
		COMMON.STEP,
		COMMON.STEP01,
		COMMON.STEP02,
		COMMON.SMIN,
		COMMON.DABSI,
		COMMON.DRLTI,
		COMMON.STEPMD,
		COMMON.TIMEND,
		COMMON.NAME,
		COMMON.nLength,
		COMMON.NSTEP,
		COMMON.SYSPRN,
		COMMON.NITER,
		COMMON.ITR,
		COMMON.CODE,
		COMMON.NUMINT,
		COMMON.NUMPP,
		COMMON.CODSTP,
		COMMON.CODGRF,
		COMMON.NEWINT,
		COMMON.MINSTP,
		COMMON.RLMAX,
		COMMON.RLMIN,
		COMMON.MSHEPS,
		COMMON.INTMAX,
		COMMON.PI,
		COMMON.REZB,
		COMMON.REZC,
		COMMON.REZD,		
		COMMON.RELYX,
		COMMON.XNMPXL,
		COMMON.YNMPXL,
		COMMON.XNMSMB,
		COMMON.YNMSMB,
		COMMON.NCOLOR,
		COMMON.NMVPAG,
		COMMON.MODES,
		COMMON.IK4,
		COMMON.IS4]

	return [comm, I, Y, X, V, A, NEW, OLD, WRK]
