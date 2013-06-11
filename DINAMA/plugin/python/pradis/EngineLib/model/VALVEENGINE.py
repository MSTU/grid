# coding=Windows-1251
#HELP<model name="ValveEngine" module="EngineLib" alias = "VALVEE" ext="5" par="1" vpr = "1" adr="2" ign ="3" wrk = "10">   
#HELP	<description>
#HELP		<russian>
#HELP 		Клапан для ДВС
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
#HELP		<parameter name="Diameter" type="real" default="0.03">
#HELP			<description>
#HELP				<russian>Диаметр клапана, м</russian>
#HELP				<english>Valve diameter, m</english>
#HELP			</description>
#HELP		</parameter>
#HELP		<parameter name="w" type="real" default="0.002">
#HELP			<description>
#HELP				<russian>Ширина седла, м</russian>
#HELP				<english>Seat width, m</english>
#HELP			</description>
#HELP		</parameter>
#HELP		<parameter name="stemDiameter" type="real" default="0.005">
#HELP			<description>
#HELP				<russian>Диаметр стержня, м</russian>
#HELP				<english>Valve stem diameter, m</english>
#HELP			</description>
#HELP		</parameter>
#HELP		<parameter name="portDiameter" type="real" default="0.025">
#HELP			<description>
#HELP				<russian>Диаметр канала, м</russian>
#HELP				<english>Valve port diameter, m</english>
#HELP			</description>
#HELP		</parameter>
#HELP		<parameter name="beta" type="real" default="45">
#HELP			<description>
#HELP				<russian>Угол седля клапана, гр.</russian>
#HELP				<english>Seat angle, grad</english>
#HELP			</description>
#HELP		</parameter>
#HELP		<parameter name="Cd" type="real" default="0,0.12,0.28,0.42,0.50,0.52,0.51,0.51,0.51,0.51">
#HELP			<description>
#HELP				<russian>Список коэффициентов истечения, 10 значений</russian>
#HELP				<english>Array of Cd discharge coefficient (0, 0.05, ... , 0.30)</english>
#HELP			</description>
#HELP		</parameter>
#HELP		<parameter name="gamma" type="real" default="1.4">
#HELP			<description>
#HELP				<russian>Тепловой коэффициент</russian>
#HELP				<english>Specific heat ratio</english>
#HELP			</description>
#HELP		</parameter>
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

class VALVEENGINE (model):

		
		
	
	def Execute(COMMON, I, Y, X, V, A, PAR, NEW, OLD, WRK):
		if COMMON.NEWINT == 1:                       
#			pl = PradisLog()
			ERR = 0



			if ERR == 1:
				if COMMON.CODE < 100.:
					COMMON.CODE = 100.

				res = return_result(COMMON, I, Y, X, V, A, NEW, OLD, WRK)
				return res

		gamma = PAR[16] 
		fp = FluidProperties([],[])
		
		Pa= PAR[17] #101000 "Reference pressure";
		T0 = fp.TG(PAR,18)+273.15
		MM = fp.MM(PAR,18)  #28.98/1000
		Rg = fp.R(PAR,18)          #8.31441; 
		Cp = fp.Cp(PAR,2)          #
		R = Rg/MM
		eps = 1e-20
		
		Pin = V[1]+Pa
		Tin = V[2]+T0
		Pout= V[3]+Pa
		Tout= V[4]+T0
		
		Ain5	= V[5]

#		print 'A=', V[5]
		
#		Ain = Ain * Cd
		(Ain, der_s)  = CdA (Ain5, PAR)
#		der_s=1.0
#		Ain = Ain5
		for i in xrange(5**2):
			Y[i+1] = 0.0
		
		if (Pout>Pin):
			sign_T = 1.0
			sign_T2 = -1.0
			P = Pout
			T = Tout
				
#			(f, derPin_f, derPout_f) = f_p (Pin, Pout)
		else:
			sign_T = 1.0
			sign_T2 = 1.0
			P = Pin
			T = Tin
#		T = 300.0	
#			(f, derPout_f, derPin_f) = f_p (Pin, Pout)
		(f, derPin_f, derPout_f) = f_p (Pin, Pout, gamma)		
		if T<eps:
			T = eps
			sign_T = 0.0
		
		b = 1.0/sqrt(R)*Ain/sqrt(T)
		d = 1.0/sqrt(R)*Ain*f
			
		der_m = b*f
		q = Cp*(Tin-Tout)*der_m*sign_T2
		
#		q = (Tin-Tout)*lambda
#		print 'b=',b,   'f=',f	
#		print 'T=', T
#		print 'd=', d
		derT_der_m = - d*0.5 * (T **(-1.5))*sign_T
#		derT_der_m = 0.0
#		print 'der_m=', der_m
		derA_der_m = 1.0/sqrt(R)/sqrt(T)*f
		derTin_q = Cp*der_m*sign_T2
		derTout_q = -derTin_q
		
		
		Y[1+0*5]  =  b*derPin_f  # Pin	
		Y[3+0*5]  =  b*derPout_f  # Pout	
		Y[5+0*5]  =  derA_der_m * der_s # A

		
		
		
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
		Y[1+1*5]  =  Cp * (Tin-Tout) * Y[1+0*5]*sign_T2# Pin
		Y[3+1*5]  =  Cp * (Tin-Tout) * Y[3+0*5]*sign_T2# Pout
		Y[2+1*5]  =  derTin_q+ Cp*Tin * Y[2+0*5]*sign_T2# Tin
		Y[4+1*5]  =  derTout_q- Cp*Tout * Y[4+0*5]*sign_T2# Tout
		Y[5+1*5]  =  Cp * (Tin-Tout)*Y[5+0*5]*sign_T2 # A
		
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

def f_p (Pin, Pout, gamma):
	if Pin > Pout:
		qm=1
	else:
		qm=-1
	qm=Pin-Pout
	qm=qm*0.1
#	return (qm, 1.0, -1.0)


	eps=1e-20
	p=Pin
	p_out = Pout
	if (Pout>Pin):
		p = Pout
		p_out = Pin

#	gamma=1.4 
	sign_p = 1.0
	sign_p_out = 1.0
	
#  //Flow functions
	p_critical =p*(2.0/(gamma + 1.0))**((gamma+1)/2.0/(gamma - 1.0));
	
#	print p_critical
	if p_critical>=p_out:
#	if -1>0:
		flowSubsonic =sqrt(gamma)*(2.0/(gamma + 1.0))**((gamma + 1.0)/(2.0*(gamma - 1.0)));
		flow = flowSubsonic
		
		der_p_g = flowSubsonic #*sign_p
		der_pout_g = 0.0
#		return (qm, 1.0, -1.0)		
	else:
#		return (qm, 1.0, -1.0)		
		if abs(p_out)<eps:
			p_out = eps
			sign_p_out=0.0
		if abs(p)<eps:
			p = eps
			sign_p=0.0
		
#		print p, ' ', pout, '==='
#		print 'aaaaaaaaaaaaa'
		kk = 1.0-p_out/p
		if (1.0-p_out/p < eps):
			kk = eps
		flowSupersonic =((p_out/p)**(1.0/gamma))*sqrt((2*gamma/(gamma - 1.0))*(1.0 - (p_out/p)**((gamma - 1.0)/gamma)));
		flow = flowSupersonic
		
			
		
		f=flowSupersonic/((p_out/p)**(1.0/gamma))
		aa= 2*gamma/(gamma-1.0)
		b=(gamma-1.0)/gamma
		
		der_p_f = sqrt(aa)*b/2.0*(kk**(b/2.0-1.0))*p_out/(p**2)*sign_p
		
		
		der_pout_f=-sqrt(aa)*b/2.0*(kk**(b/2.0-1.0))/(p)*sign_p_out
		
		
		der_p_g=(p_out**(1.0/gamma))*(f*(1-1/gamma)*(p**(-1.0/gamma))+ 
				(p**(1.0-1.0/gamma))*der_p_f)*sign_p
		der_pout_g = (p**(1-1.0/gamma))*(f/gamma*(p_out**(1.0/gamma - 1.0)) + (p_out**(1/gamma))*der_pout_f )*sign_p_out
		
	m_flow = p*flow;
	
	
		#	print 'f_p calling'
	if Pin >= Pout:
		return (m_flow, der_p_g, der_pout_g)
	else:
		return (-m_flow, -der_pout_g, -der_p_g)
#	qm=Pin-Pout
#	qm=qm*0.1
#	return (qm, 1.0, -1.0)

def CdA (lift_s, par):
	
	diameter =par[1]
	w = par[2]
	stemDiam=par[3]
	portDiam=par[4]
	beta=par[5]
	arrayCd=[par[6],par[7],par[8],par[9],par[10],par[11],par[12], par[13],par[14], par[15]]
	
#	print 'Cd= ', arrayCd
#  //Find Cd
	lenCd = len (arrayCd)
	ratio =lift_s/diameter;
	
	
	
	percentFloor =int(ratio/ 0.05); #// result - 1 to 9
	derCd =0.0
	
	
	
	if percentFloor>=lenCd-1:
		percentFloor = lenCd-1
		Cd = arrayCd[lenCd-1]
	elif percentFloor<0:
		percentFloor = 0
		Cd = arrayCd[0]
	else:
		d=ratio/0.05-percentFloor
		Cd =arrayCd[percentFloor] + (arrayCd[percentFloor + 1] - arrayCd[percentFloor])*d
		derCd =(arrayCd[percentFloor + 1] - arrayCd[percentFloor])/0.05
	
	
#  //Flow area
	betaRad =math.pi*beta/180.0;
	midDiam =diameter - w;
	
	firstAreaCondition =w/(sin(betaRad)*cos(betaRad));
	secondAreaCondition =sqrt(((portDiam**2 - stemDiam**2)/(4*midDiam))**2 - w**2) + w*tan(betaRad);
	
	
	
	Area = 0.0
	der_s_Area = 0.0
#	print '----------------',Cd
	
	
	if lift_s<0.0:
#		print '00000000', firstAreaCondition
#		return (lift_s, 1.0)
		Area = 0.0
		der_s_Area = 0.0
	
	elif lift_s<firstAreaCondition:
#		print '11111111111111', firstAreaCondition
#		return (lift_s, 1.0)
		Area =pi*lift_s*cos(betaRad)*(diameter - 2*w + lift_s*sin(2*betaRad)/2.0);
		der_s_Area =pi*cos(betaRad)*(diameter-2*w + lift_s*sin(2*betaRad))
	
	
	
	elif lift_s>=firstAreaCondition and lift_s<=secondAreaCondition:
#		print '2222222222222222', lift_s
#		return (lift_s, 1.0)
	
		Area =pi*midDiam*sqrt((lift_s - w*tan(betaRad))**2 + w**2);
		der_s_Area  = Area * 2.0*(lift_s - w*tan(betaRad))
	
	
	
	else:# lift_s>secondAreaCondition :
#		print '3333333333333', lift_s
#		return (lift_s, 1.0)
		Area =0.25*pi*(portDiam**2 - stemDiam**2);
		der_s_Area = 0.0
#	print '9999999999999', firstAreaCondition
#	return (lift_s, 1.0)
	Ar = Cd*Area
	der_sa = derCd * Area+Cd*der_s_Area

	
	return (Ar, der_sa)
	


  