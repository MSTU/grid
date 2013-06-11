import pradis.engine.functions as f
import math
import string
import random
import numpy
import scipy
import af
import glb
import time
from misc import *
from ParameterValues import *
from string import *
from scipy import interpolate

class UserRoad (ParameterValues):
#------------------------------------getting variables--------------------------------------
	def __init__ (self, nl, pl, desc= misc.default):		
		self.values = pl
		pM=pl[0]
		pN=pl[1]
		pZ=pl[2]
		w_road=pl[3]
		pF=pl[4]
		RoadLength=pl[5]
		Flag=pl[6]
		Speed=pl[7]
		WheelBase=pl[8]
		SumLength=pF[-2]
		NumRep=int(RoadLength/SumLength)
		LengthSeg=RoadLength%SumLength
		T= f.getTransformationMatrix(pM,pN,pZ)
#------------------------------------function declarations-----------------------------------		
		def writeRoad (p):
			Filehandle = open (desc+".road", 'w')
			Filehandle.write(desc+"\n")
			Filehandle.write (string.ljust('X', 38))
			Filehandle.write ('Y\n')
			count=0
			while count<len(p):
				Filehandle.write (string.rjust(str(p[count][0]), 38))
				Filehandle.write (string.rjust(str(p[count][2]), 38))
				Filehandle.write ("\n")
				count+=1
			Filehandle.close ()
		def facet (p,Np,Nt):									#Generator dannyh dlia faceta
			k=0
			road_model=[Np,Nt]
			while k < len(p):
				road_model=road_model+[p[k][0],p[k][1]+w_road/2,p[k][2]]
				road_model=road_model+[p[k][0],p[k][1]-w_road/2,p[k][2]]
				k+=1
		
			n=1
			while n < Np-2:
				road_model=road_model+[n,n+1,n+2]
				road_model=road_model+[n+2,n+1,n+3]
				n+=2
			return road_model
		
		def stand (p,v,b):										#Generator dannyh dlia stenda
			tval=[p[0][0]/v]									#Os' vremeni
			zval=[p[0][2]]										#Os' pod'ema kolesa
			position=1
			while position<len(p):
				tval=tval+[p[position][0]/v]
				zval=zval+[p[position][2]]
				position+=1
			tnew = numpy.arange(0, tval[-1], 1e-2, dtype = None)
			f = interpolate.interp1d(tval, zval)
			tck = scipy.interpolate.splrep(tnew,f(tnew),s=0)
			znew = interpolate.splev(tnew,tck,der=1)
			position=0
			if b!=0:
				stand_model=[tnew[0],round(znew[0],20)]
			else:
				stand_model=[tnew[0],round(znew[0],20)]
				position=1
			while position<len(tnew):
				stand_model=stand_model+[tnew[position]+b/v,round(znew[position],20)]
				position+=1
			return stand_model	
#------------------------------------main function-----------------------------------			
		p1=[]
		m=0
		count=0
		while m<NumRep+1:
			a=0
			if pF[1]!=pF[-1] or m==0:
				i=0
			else:
				i=2
			while i < len(pF):
				if pF[i]+m*SumLength<RoadLength:
					p1.append([pF[i]+m*SumLength])
					p1[count].append(0.0)
					p1[count].append(pF[i+1])
					i+=2
					a+=1
					count+=1
				else:
					p1.append([RoadLength])
					p1[count].append(0.0)
					p1[count].append(1.0*(pF[i-1]-(pF[i-1]-pF[i+1])*(RoadLength*1.0-pF[i-2]-(m)*SumLength)/(pF[i]-pF[i-2])))
							
					count+=1
					break
			m+=1
		writeRoad (p1)
		Npoints=count*2
		Ntriangles=Npoints-2

		j=0
		while j < len(p1):
			p1[j]=f.getPoint(p1[j],T,pM)
			j+=1
		if Flag=='Facet':
			self.values = facet(p1,Npoints,Ntriangles)
		else:
			if Flag=='Stand':
				self.values = stand (p1,Speed,WheelBase)
			else:
				print "Wrong parameter Flag"	
#------------------------------------return result of the object------------------------------------
	def Values(self):
		return self.values		
			



