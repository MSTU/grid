# coding=Windows-1251
# Клапан с универсальным управлением
#HELP<model name="Valve" module="EngineLib" alias = "VALVE" ext="5" par="1" vpr = "1" adr="2" ign ="3" wrk = "10">   
#HELP	<description>
#HELP		<russian>
#HELP 		Клапан 
#HELP		</russian>
#HELP		<english>The description of M3D image</english>
#HELP	</description>
#HELP	<nodelist>
#HELP		<node name="In" type="EngineLib.ThermalFluid">
#HELP			<description>
#HELP				<russian>Вход клапана</russian>
#HELP				<english>The description of M3D image</english>
#HELP			</description>
#HELP   	</node>
#HELP		<node name="Out" type="EngineLib.ThermalFluid">
#HELP			<description>
#HELP				<russian>Выход клапана</russian>
#HELP				<english>The description of M3D image</english>
#HELP			</description>
#HELP   	</node>
#HELP		<node name="valve_lift" type="base.DOF1">
#HELP			<description>
#HELP				<russian>Ход клапана</russian>
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
#HELP		<parameter name="Fluid" type="list" default="">
#HELP			<description>
#HELP				<russian>Свойства жидкости</russian>
#HELP				<english>Inertia coefficient (mass)</english>
#HELP			</description>
#HELP		</parameter>
#HELP	</parameterlist>
#HELP	<worklist>
#HELP	</worklist>
#HELP	<statelist>
#HELP	</statelist>
#HELP	<image2d icon = "EngineLib.Valve" symbol = ""/>	
#HELP</model> 

from pradis.ppl.model import *
#from PradisLog import *
from array import *
from  pradis.EngineLib.FluidProperties import *
from math import *

class VALVE (model):

		
		
	
	def Execute(COMMON, I, Y, X, V, A, PAR, NEW, OLD, WRK):
		if COMMON.NEWINT == 1:                       
#			pl = PradisLog()
			ERR = 0



			if ERR == 1:
				if COMMON.CODE < 100.:
					COMMON.CODE = 100.

				res = return_result(COMMON, I, Y, X, V, A, NEW, OLD, WRK)
				return res

		fp = FluidProperties([],[])
		
		Pa= PAR[1] #101000 "Reference pressure";
		T0 = fp.TG(PAR,2)+273.15
		MM = fp.MM(PAR,2)  #28.98/1000
		Rg = fp.R(PAR,2)          #8.31441; 
		R = Rg/MM
		eps = 1e-20
		
		Pin = V[1]+Pa
		Tin = V[2]+T0
		Pout= V[3]+Pa
		Tout= V[4]+T0
		
		Ain	= V[5]

#		print 'A=', V[5]
		
		for i in xrange(5**2):
			Y[i+1] = 0.0
		
		if (Pout>Pin):
			sign_T = 1.0
			P = Pout
			T = Tout
				
#			(f, derPin_f, derPout_f) = f_p (Pin, Pout)
		else:
			sign_T = 1.0
			P = Pin
			T = Tin
#		T = 300.0	
#			(f, derPout_f, derPin_f) = f_p (Pin, Pout)
		(f, derPin_f, derPout_f) = f_p (Pin, Pout)		
		if T<eps:
			T = eps
			sign_T = 0.0
		
		b = 1.0/sqrt(R)*Ain/sqrt(T)
		d = 1.0/sqrt(R)*Ain*f
			
		der_m = b*f
		q = - Rg*(Tin-Tout)*der_m
#		q = (Tin-Tout)*lambda
#		print 'b=',b,   'f=',f	
#		print 'T=', T
#		print 'd=', d
		derT_der_m = - d*0.5 * (T **(-1.5))*sign_T
#		derT_der_m = 0.0
#		print 'der_m=', der_m
		derA_der_m = 1.0/sqrt(R)/sqrt(T)*f
		derTin_q = -Rg*der_m
		derTout_q = -derTin_q
		
		
		Y[1+0*5]  =  b*derPin_f  # Pin	
		Y[3+0*5]  =  b*derPout_f  # Pout	
		Y[5+0*5]  =  derA_der_m  # A

		
		
		
		if (Pout>Pin):
		# I[1] p
			Y[2+0*5]  =  0.0  # Tin
			Y[4+0*5]  =  derT_der_m  # Tout
		# I[2] T
#			Y[2+1*5]  =  0.0 # Tin
#			Y[4+1*5]  =  Rg*b*f*sign_T # Tout
		else:
		# I[1] p
			Y[2+0*5]  =  derT_der_m  # Tin
			Y[4+0*5]  =  0.0  # Tout
		# I[2] T
#			Y[2+1*5]  =  Rg*b*f*sign_T # Tin
#			Y[4+1*5]  =  0.0 # Tout

		#I[2]
		Y[1+1*5]  =  -Rg * (Tin-Tout) * Y[1+0*5]# Pin
		Y[3+1*5]  =  -Rg * (Tin-Tout) * Y[3+0*5]# Pout
		Y[2+1*5]  =  derTin_q+ Rg*Tout * Y[2+0*5]# Tin
		Y[4+1*5]  =  derTout_q- Rg*Tin * Y[4+0*5]# Tout
		Y[5+1*5]  =  - Rg * (Tin-Tout)*Y[5+0*5] # A
		
		I[1]  =  der_m
		I[2]  =  q
		I[3]  =  - I[1]
		I[4]  =  - I[2]
		I[5]  =  0.0
		
		WRK [1] = der_m
		WRK [2] = q
		
		
		# I[3] p
		Y[1+2*5]  =  -Y[1+0*5]
		Y[2+2*5]  =  -Y[2+0*5]
		Y[3+2*5]  =  -Y[3+0*5]
		Y[4+2*5]  =  -Y[4+0*5]
		Y[5+2*5]  =  -Y[5+0*5]
		
		# I[4] T
		Y[1+3*5]  =  -Y[1+1*5]
		Y[2+3*5]  =  -Y[2+1*5]
		Y[3+3*5]  =  -Y[3+1*5]
		Y[4+3*5]  =  -Y[4+1*5]
		Y[5+3*5]  =  -Y[5+1*5]
		
#		print 'I[1]=', I[1]
		
		res = return_result(COMMON, I, Y, X, V, A, NEW, OLD, WRK)
		return res

def f_p (Pin, Pout):
		
#	print 'f_p calling'
	if Pin > Pout:
		qm=1
	else:
		qm=-1
	qm=Pin-Pout
	qm=qm*0.1
	return (qm, 1.0, -1.0)
