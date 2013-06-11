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

class TrapezeRoad (ParameterValues):
#------------------------------------getting variables--------------------------------------
	def __init__ (self, nl, pl, desc= misc.default):
		self.values = pl
		pM=pl[0]
		pN=pl[1]
		pZ=pl[2]
		w_road=pl[3]
		start=pl[4]
		UpFrontLength=pl[5]
		height=pl[6]
		length=pl[7]
		DownFrontLength=pl[8]
		FinishHeight=pl[9]
		end=pl[10]
		RoadLength=pl[11]
		Flag=pl[12]
		Speed=pl[13]
		WheelBase=pl[14]
		SumLength=start+UpFrontLength+length+DownFrontLength+end
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
		i=0.0
		offset=0
		while i<NumRep:
			offset=i*SumLength
			if i==0:
				p1=p1+[[0,0,0],[offset+start,0,0],[offset+start+UpFrontLength,0,height],[offset+start+UpFrontLength+length,0,height],[offset+start+UpFrontLength+length+DownFrontLength,0,FinishHeight],[offset+start+UpFrontLength+length+DownFrontLength+end,0,FinishHeight]]
			else:
				if FinishHeight==0:
					p1=p1+[[offset+start,0,0],[offset+start+UpFrontLength,0,height],[offset+start+UpFrontLength+length,0,height],[offset+start+UpFrontLength+length+DownFrontLength,0,FinishHeight],[offset+start+UpFrontLength+length+DownFrontLength+end,0,FinishHeight]]
				else:
					p1=p1+[[offset,0,0],[offset+start,0,0],[offset+start+UpFrontLength,0,height],[offset+start+UpFrontLength+length,0,height],[offset+start+UpFrontLength+length+DownFrontLength,0,FinishHeight],[offset+start+UpFrontLength+length+DownFrontLength+end,0,FinishHeight]]
			i+=1
		if LengthSeg!=0:
			offset=i*SumLength
			if FinishHeight!=0 or NumRep==0:
				p1=p1+[[offset,0,0]]
			if LengthSeg<=start:
				p1=p1+[[offset+LengthSeg,0,0]]
			else:
				if LengthSeg<=start+UpFrontLength:
					p1=p1+[[offset+start,0,0],[offset+LengthSeg,0,height*(LengthSeg-start)/UpFrontLength]]
				else:
					if LengthSeg<=start+UpFrontLength+length:
						p1=p1+[[offset+start,0,0],[offset+start+UpFrontLength,0,height],[offset+LengthSeg,0,height]]
					else:
						if LengthSeg<=start+UpFrontLength+length+DownFrontLength:
							p1=p1+[[offset+start,0,0],[offset+start+UpFrontLength,0,height],[offset+start+UpFrontLength+length,0,height],[offset+LengthSeg,0,height-(height-FinishHeight)*(LengthSeg-start-UpFrontLength-length)/DownFrontLength]]
						else:
							p1=p1+[[offset+start,0,0],[offset+start+UpFrontLength,0,height],[offset+start+UpFrontLength+length,0,height],[offset+start+UpFrontLength+length+DownFrontLength,0,FinishHeight],[offset+LengthSeg,0,FinishHeight]]
					
		writeRoad (p1)
		j=0
		while j < len(p1):
			p1[j]=f.getPoint(p1[j],T,pM)
			j+=1
		Npoints=2*len(p1)
		Ntriangles=Npoints-2
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
			



