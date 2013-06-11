# coding=Windows-1251
#HELP<model name="Reaction" module="EngineLib" alias = "REACTI" ext="6" par="1" vpr = "1" adr="2" ign ="0" wrk = "10">   
#HELP	<description>
#HELP		<russian>
#HELP 		Расчет кинетики химической реакции из 4-х компонент aA+bB=cC+dD
#HELP		</russian>
#HELP		<english>The description of M3D image</english>
#HELP	</description>
#HELP	<nodelist>
#HELP		<node name="pT" type="EngineLib.ThermalFluid">
#HELP			<description>
#HELP				<russian>Вход условия протекания реакции</russian>
#HELP				<english>The description of M3D image</english>
#HELP			</description>
#HELP   	</node>
#HELP		<node name="pA" type="base.DOF1">
#HELP			<description>
#HELP				<russian>Парциальное давление компоненты А</russian>
#HELP				<english>The description of M3D image</english>
#HELP			</description>
#HELP   	</node>
#HELP		<node name="pB" type="base.DOF1">
#HELP			<description>
#HELP				<russian>Парциальное давление компоненты B</russian>
#HELP				<english>The description of M3D image</english>
#HELP			</description>
#HELP   	</node>
#HELP		<node name="pC" type="base.DOF1">
#HELP			<description>
#HELP				<russian>Парциальное давление компоненты C</russian>
#HELP				<english>The description of M3D image</english>
#HELP			</description>
#HELP   	</node>
#HELP		<node name="pD" type="base.DOF1">
#HELP			<description>
#HELP				<russian>Парциальное давление компоненты D</russian>
#HELP				<english>The description of M3D image</english>
#HELP			</description>
#HELP   	</node>
#HELP	</nodelist>
#HELP	<parameterlist>
#HELP		<parameter name="Pa" type="real" default="101000">
#HELP			<description>
#HELP				<russian>Давление атмосферное, Па</russian>
#HELP				<english>Inertia coefficient (mass)</english>
#HELP			</description>
#HELP		</parameter>
#HELP		<parameter name="a" type="real" default="1">
#HELP			<description>
#HELP				<russian>Стехиометрическое количество вещества А</russian>
#HELP				<english>Inertia coefficient (mass)</english>
#HELP			</description>
#HELP		</parameter>
#HELP		<parameter name="b" type="real" default="1">
#HELP			<description>
#HELP				<russian>Стехиометрическое количество вещества B</russian>
#HELP				<english>Inertia coefficient (mass)</english>
#HELP			</description>
#HELP		</parameter>
#HELP		<parameter name="c" type="real" default="1">
#HELP			<description>
#HELP				<russian>Стехиометрическое количество вещества C</russian>
#HELP				<english>Inertia coefficient (mass)</english>
#HELP			</description>
#HELP		</parameter>
#HELP		<parameter name="d" type="real" default="1">
#HELP			<description>
#HELP				<russian>Стехиометрическое количество вещества D</russian>
#HELP				<english>Inertia coefficient (mass)</english>
#HELP			</description>
#HELP		</parameter>
#HELP		<parameter name="lgKv" type="real" default="0,1,1,1,0">
#HELP			<description>
#HELP				<russian>lg Константы скорости прямой реакции, зависимость от температуры (K)</russian>
#HELP				<english>Inertia coefficient (mass)</english>
#HELP			</description>
#HELP		</parameter>
#HELP		<parameter name="lgKr" type="real" default="0,-1,1,-1,0">
#HELP			<description>
#HELP				<russian>lg Константы скорости обратной реакции, зависимость от температуры (K). Kr=0 для прямой реакции, Kr=1 для равновесной реакции</russian>
#HELP				<english>Inertia coefficient (mass)</english>
#HELP			</description>
#HELP		</parameter>
#HELP	</parameterlist>
#HELP	<worklist>
#HELP	</worklist>
#HELP	<statelist>
#HELP	</statelist>
#HELP	<image2d icon = "EngineLib.Reaction" symbol = ""/>	
#HELP</model> 

from pradis.ppl.model import *
#from PradisLog import *
from array import *
#from  pradis.EngineLib.FluidProperties import *
from math import *

class REACTION(model):

		
		
	
	def Execute(COMMON, I, Y, X, V, A, PAR, NEW, OLD, WRK):
		try:
		
			if COMMON.NEWINT == 1:                       
	#			pl = PradisLog()
				ERR = 0



				if ERR == 1:
					if COMMON.CODE < 100.:
						COMMON.CODE = 100.

					res = return_result(COMMON, I, Y, X, V, A, NEW, OLD, WRK)
					return res

			
			Pa= PAR[1] #101000 "Reference pressure";
	#		Ta= PAR[2] # "Reference temperature";

			Ma= PAR[2] # 
			Mb= PAR[3] # 
			Mc= PAR[4] # 
			Md= PAR[5] # 
			
			print 'start:1                ***'
			
			(Kv, Kr) = getK (PAR, 6)
			print 'Kv=', Kv
			print 'Kr=', Kr
			

			eps = 1e-20
			
			Pin = V[1]+Pa
			Tin = V[2]+273.15
			
			pA	= V[3]+Pa
			der_pA = A[3]
			pB	= V[4]+Pa
			der_pB = A[4]
			pC	= V[5]+Pa
			der_pC = A[5]
			pD	= V[6]+Pa
			der_pD = A[6]

			k = 1.3806504e-23 # Bolzmann constant
			
	#		print 'A=', V[5]

			if Tin < eps:
				Tin = eps
			
			nA = pA/k/Tin
			nB = pB/k/Tin
			nC = pC/k/Tin
			nD = pD/k/Tin

			print 'nA=',nA, ' nB=',nB, ' nC=',nC
			
			(kv, derT_kv) = velocity (Kv, Tin)
			(kr, derT_kr) = velocity (Kr, Tin)
			
			print 'kv=',kv,'  kr=',kr
			
			a=nA**Ma
			b=nB**Mb
			c=nC**Mc
			d=nD**Md
			
			q = (-kv*a*b+kr*c*d)*k*Tin
			qA = q
			qB = q
			qC = -q
			qD = -q
			
			print '5: q=',q
			
			kt=1.0/k/Tin
			

			if Ma==0:
				derA_q=0.0
			else:
				derA_q=(-kt*kv*b*Ma*(nA**(Ma-1)))*k*Tin
			if Mb==0:
				derB_q=0.0
			else:
				derB_q=(-kt*kv*a*Mb*(nB**(Mb-1)))*k*Tin
			if Mc==0:
				derC_q=0.0
			else:
				derC_q=(kt*kr*d*Mc*(nC**(Mc-1)))*k*Tin
			if Md==0:
				derD_q=0.0
			else:
				derD_q=(kt*kr*c*Md*(nD**(Md-1)))*k*Tin

			derT_q = (-derT_kv*a*b+derT_kr*c*d)*k*Tin+(-kv*a*b+kr*c*d)*k
				
			I[1]  =  0.0
			I[2]  =  0.0
			I[3]  =  -der_pA+qA
			I[4]  =  -der_pB+qB
			I[5]  =  -der_pC+qC
			I[6]  =  -der_pD+qD
			
			print '6: der_pA = ', der_pA,  ' I[3]=', I[3]
			
			NN=6
			for i in xrange(NN**2*2):
				Y[i+1] = 0.0


			dya = NN*NN
				
			#I[3]
			Y[2+2*NN]  =  derT_q
			Y[3+2*NN]  =  derA_q
			Y[4+2*NN]  =  derB_q
			Y[5+2*NN]  =  derC_q
			Y[6+2*NN]  =  derD_q
			
			Y[3+2*NN+dya]  =  -1.0

			#I[4]
			Y[2+3*NN]  =  derT_q
			Y[3+3*NN]  =  derA_q
			Y[4+3*NN]  =  derB_q
			Y[5+3*NN]  =  derC_q
			Y[6+3*NN]  =  derD_q
			
			Y[4+3*NN+dya]  =  -1.0

			#I[5]
			Y[2+4*NN]  =  -derT_q
			Y[3+4*NN]  =  -derA_q
			Y[4+4*NN]  =  -derB_q
			Y[5+4*NN]  =  -derC_q
			Y[6+4*NN]  =  -derD_q
			
			Y[5+4*NN+dya]  =  -1.0

			#I[6]
			Y[2+5*NN]  =  -derT_q
			Y[3+5*NN]  =  -derA_q
			Y[4+5*NN]  =  -derB_q
			Y[5+5*NN]  =  -derC_q
			Y[6+5*NN]  =  -derD_q

			Y[6+5*NN+dya]  =  -1.0
			
			res = return_result(COMMON, I, Y, X, V, A, NEW, OLD, WRK)
			return res
		except e:
			print e.GetError()
		

		
def getK (PAR, npar)		:
	eps = 1e-20
	nlen = len (PAR)
	Kv = []
	nv = 0
#	print 'nlen = ', nlen
	for i in xrange (npar, nlen, 2):
		t=PAR[i]
#		print 't=', t, 'i=',i
		if (t<eps):
			break
		k = PAR[i+1]
		Kv.append ( (t,k) )
		nv+=2

	Kr=[]
	for i in xrange (nv+1+npar, nlen, 2):
		t=PAR[i]
#		print 'i2=',i, '  t2=', t
		if (t<eps):
			break
		k = PAR[i+1]
		Kr.append ( (t,k) )

#	print 'Kv=', Kv
#	print 'Kr=', Kr
	
	return (Kv, Kr)

	
def velocity (K, T):
	nlen = len (K)
	n=-1
	
	print 'start velocity'
	for i in xrange (nlen):
		(t,k) = K[i]
		
		print '(k,t)=', (k,t), ' T=', T
		n=i
		if (t>=T):
			
			print 11111
			break
		print 22222
		
	print 3333
	if n <0:
		return (0.,0.)
#	elif n==nlen-1:
#		n=nlen-2
	elif nlen == 1:
		(t1,k1)=K[n]
		(t2,k2)=K[n]
		t2+=1.
	elif n == 0:
		(t1,k1)=K[n]
		(t2,k2)=K[n+1]
	else:
		(t1,k1)=K[n-1]
		(t2,k2)=K[n]
	print '1:(k,t)=', (k1,t1)
	print '2:(k,t)=', (k2,t2)

	Kvel = (k1+(k2-k1)*(T-t1)/(t2-t1))
	
	print '3: Kvel=', Kvel
	if Kvel >20.:
		Kder = log(10.0)*(10.**20.)*  (k2-k1)/(t2-t1)
		Kvel = Kder * (Kvel-20.)+10.**20.0
	else:
		Kvel = 10** Kvel
		Kder = log(10.0)*Kvel*  (k2-k1)/(t2-t1)
		
#	Kvel =   (k1 + (k2-k1)*(T-t1))
	
#	print 'Kder=', Kder
	
#	print 
		
	print 'Kve1=', Kvel, '  Kder = ', Kder
#	return (1., 1.)
	
	return (Kvel, Kder)












