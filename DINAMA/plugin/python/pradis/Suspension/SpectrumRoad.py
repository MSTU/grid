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

class SpectrumRoad (ParameterValues):
#------------------------------------getting variables--------------------------------------
	def __init__ (self, nl, pl, desc= misc.default):
		self.values = pl
		pM=pl[0]
		pN=pl[1]
		pZ=pl[2]
		w_road=pl[3]
		Spectrum=pl[4]
		File=pl[5]
		Step=pl[6]
		RoadLength=pl[7]
		M=pl[8]
		Flag=pl[9]
		Speed=pl[10]
		WheelBase=pl[11]
		
		if File!='':	
			Spectrum_File=open (File, 'r')
			temp=Spectrum_File.read()
			Spectrum=map(float,temp.split(','))
			Spectrum_File.close ()
		N=RoadLength/Step
#		dw=(Spectrum[-2]-Spectrum[0])/M
		w0=2*math.pi/RoadLength
#		w0=math.pi*((Spectrum[-2])/M)
#		w0=(Spectrum[-2])/M
		dw = w0
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
		def spec (a):
			i=0
			less=0
			well=-1
			more=-1
			while i<len(Spectrum):
				if a==Spectrum[i]:
					well=i
					return Spectrum[well+1]
					break
				i+=2
			if well==-1 and a>Spectrum[0]:
				i=0
				while i<len(Spectrum):
					if a>Spectrum[i]:
						less=i
					i+=2
				i=less
				while i<len(Spectrum):
					if a<Spectrum[i]:
						more=i
						break
					i+=2
			elif well==-1 and a<Spectrum[0]:
				less=0
				more=2
			elif well==-1 and a>Spectrum[-2]:
				less=-4
				more=-2
			
			if	well==-1:
					k=float(Spectrum[more+1]-Spectrum[less+1])/float(Spectrum[more]-Spectrum[less])
					b=Spectrum[less+1]-k*Spectrum[less]
					return k*a+b
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
			tnew = numpy.arange(0, tval[-1], 1e-3, dtype = None)
			f = interpolate.interp1d(tval, zval)
			tck = scipy.interpolate.splrep(tnew,f(tnew),s=0)
			znew = interpolate.splev(tnew,tck,der=0)
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
		pF=[]
		n=0					
		while n<=N:
			pF.append(n*Step)
			pF.append(0.0)
			n+=1
		
		m=0
		ke = 1.0
		phase=math.pi*random.uniform(-1.0,1.0)
		while m<=M:
#			sx=spec(m*dw)
			sx=spec(m*dw/2/math.pi)
			sq =math.sqrt(2.0*dw*sx/2/math.pi)
#			sq =math.sqrt(2.0*dw*sx)
#			sq =math.sqrt(sx)
			n=0
			phase=math.pi*random.uniform(-1.0,1.0)
			if sq!=0:
				while n<=N:
					#phase=math.pi*random.uniform(-1, 1)
					pF[2*n+1]=pF[2*n+1]+sq*math.cos(m*dw*n*Step+phase)
					#pF[(n*2)+1]=pF[(n*2)+1]+0.1*math.sqrt(2.0*sx)*math.cos(2.0*math.pi*(m*dw+w0)*n*Step+phase)
					n+=1
			m+=1
		p1=[]
		i = 0
		count=0
		while i < len(pF):
			p1.append([pF[i]])
			p1[count].append(0.0)
			p1[count].append(pF[i+1])
			i+=2
			count+=1
		Npoints=count*2
		Ntriangles=Npoints-2
		j=0
		writeRoad(p1)
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
			



