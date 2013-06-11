# coding=Windows-1251
# С уравнениями массы
#HELP<model name="CombustionWiebe" module="EngineLib" alias = "COMBUS" vpr="1" ext="7" ent="3" par="10" adr="1" wrk = "12" str = "4" ign = "0">   
#HELP	<description>
#HELP		<russian>
#HELP 		Камера сгорания на основе закона Вибе 
#HELP		</russian>
#HELP		<english>The description of M3D image</english>
#HELP	</description>
#HELP	<nodelist>
#HELP		<node name="Chamber" type="EngineLib.ThermalFluid">
#HELP			<description>
#HELP				<russian>Состояние в камере сгорания</russian>
#HELP				<english>The description of M3D image</english>
#HELP			</description>
#HELP   	</node>
#HELP		<node name="spark" type="base.DOF1">
#HELP			<description>
#HELP				<russian>Сигнал искры</russian>
#HELP				<english>The description of M3D image</english>
#HELP			</description>
#HELP   	</node>
#HELP		<node name="Piston" type="base.DOF1">
#HELP			<description>
#HELP				<russian>Ход поршня</russian>
#HELP				<english>The description of M3D image</english>
#HELP			</description>
#HELP   	</node>
#HELP		<node name="Crank" type="base.DOF1">
#HELP			<description>
#HELP				<russian>Коворот коленчатого вала</russian>
#HELP				<english>The description of M3D image</english>
#HELP			</description>
#HELP   	</node>
#HELP		<node name="heatPort" type="base.DOF1">
#HELP			<description>
#HELP				<russian>Тепловой поток</russian>
#HELP				<english>The description of M3D image</english>
#HELP			</description>
#HELP   	</node>
#HELP		<node name="Gc_cylinder" type="base.DOF1">
#HELP			<description>
#HELP				<russian>Gc_cylinder</russian>
#HELP				<english>The description of M3D image</english>
#HELP			</description>
#HELP   	</node>
#HELP	</nodelist>
#HELP	<parameterlist>
#HELP		<parameter name="Bore" type="real" default="0.05">
#HELP			<description>
#HELP				<russian>Диаметр поршня</russian>
#HELP				<english>Inertia coefficient (mass)</english>
#HELP			</description>
#HELP		</parameter>
#HELP		<parameter name="Stroke" type="real" default="0.05">
#HELP			<description>
#HELP				<russian>Ход поршня</russian>
#HELP				<english>Inertia coefficient (mass)</english>
#HELP			</description>
#HELP		</parameter>

#HELP		<parameter name="comp_ratio" type="real" default="0.05">
#HELP			<description>
#HELP				<russian>Коэффициент сжатия</russian>
#HELP				<english>Inertia coefficient (mass)</english>
#HELP			</description>
#HELP		</parameter>
#HELP		<parameter name="lhv" type="real" default="44e+6">
#HELP			<description>
#HELP				<russian>Низшая теплота сгорания топливной смеси</russian>
#HELP				<english>Inertia coefficient (mass)</english>
#HELP			</description>
#HELP		</parameter>
#HELP		<parameter name="afr" type="real" default="14.7">
#HELP			<description>
#HELP				<russian>Стехиометрическое количество воздуха</russian>
#HELP				<english>Air/Fuel Ratio</english>
#HELP			</description>
#HELP		</parameter>
#HELP		<parameter name="burn_duration" type="real" default="60">
#HELP			<description>
#HELP				<russian>Длительность сгорания, гр.</russian>
#HELP				<english>Inertia coefficient (mass)</english>
#HELP			</description>
#HELP		</parameter>
#HELP		<parameter name="Pcc" type="real" default="800.0">
#HELP			<description>
#HELP				<russian>Давление в картере относительное, Па</russian>
#HELP				<english>Inertia coefficient (mass)</english>
#HELP			</description>
#HELP		</parameter>
#HELP		<parameter name="Pa" type="real" default="101000">
#HELP			<description>
#HELP				<russian>Давление атмосферное, Па</russian>
#HELP				<english>Inertia coefficient (mass)</english>
#HELP			</description>
#HELP		</parameter>
#HELP		<parameter name="wiebe_a" type="real" default="6.908">
#HELP			<description>
#HELP				<russian>Коэффициент Вибе в законе Вибе, гр.</russian>
#HELP				<english>Inertia coefficient (mass)</english>
#HELP			</description>
#HELP		</parameter>
#HELP		<parameter name="wiebe_m" type="real" default="4">
#HELP			<description>
#HELP				<russian>Показатель m в законе Вибе</russian>
#HELP				<english>Inertia coefficient (mass)</english>
#HELP			</description>
#HELP		</parameter>
#HELP		<parameter name="alfa" type="real" default="1">
#HELP			<description>
#HELP				<russian>Коэффициент избытка воздуха</russian>
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
#HELP		<parameter name="m" type="real" default="">
#HELP			<description>
#HELP				<russian>Масса смеси в камере сгорания</russian>
#HELP				<english>Inertia coefficient (mass)</english>
#HELP			</description>
#HELP		</parameter>
#HELP		<parameter name="der_m" type="real" default="">
#HELP			<description>
#HELP				<russian>Производная массы смеси в камере сгорания</russian>
#HELP				<english>Inertia coefficient (mass)</english>
#HELP			</description>
#HELP		</parameter>
#HELP		<parameter name="V" type="real" default="">
#HELP			<description>
#HELP				<russian>Текущий объем камеры сгорания</russian>
#HELP				<english>Inertia coefficient (mass)</english>
#HELP			</description>
#HELP		</parameter>
#HELP		<parameter name="der_V" type="real" default="">
#HELP			<description>
#HELP				<russian>Производная текущего объема камеры сгорания</russian>
#HELP				<english>Inertia coefficient (mass)</english>
#HELP			</description>
#HELP		</parameter>
#HELP	</worklist>
#HELP	<statelist>
#HELP	</statelist>
#HELP	<image2d icon = "EngineLib.CombustionWiebe" symbol = ""/>	
#HELP</model> 

from pradis.ppl.model import *
#from PradisLog import *
from array import *
from  pradis.EngineLib.FluidProperties import *
from math import *

class COMBUSTIONWIEBE (model):

	
	def Execute(COMMON, I, Y, X, V, A, PAR, NEW, OLD, WRK):

		# print 'start'
		
		if COMMON.NSTEP == 0:                       
#			pl = PradisLog()
			ERR = 0

			NEW [1] = 0.0
			NEW [2] = 0.0
			NEW [3] = 0.0
			NEW [4] = 0.0
			OLD [1] = 0.0
			OLD [2] = 0.0
			OLD [3] = 0.0
			OLD [4] = 0.0

			if ERR == 1:
				if COMMON.CODE < 100.:
					COMMON.CODE = 100.

				res = return_result(COMMON, I, Y, X, V, A, NEW, OLD, WRK)
				return res

		Next = 10
		
		bore = PAR[1]		# Piston diameter
		stroke = PAR[2]		# Piston stroke
#    conrod  = PAR[3]	# conrod length
		comp_ratio= PAR[3] #9.5 "Compression ratio";
		lhv = PAR[4] #44e+6      "Fuel lower heating value";
		afr=PAR[5]   #14.7 "Стехиометрическое Air/Fuel Ratio";
		burn_duration=PAR[6]*math.pi/180.0 #60       "Duration of combustion";
		Pcc= PAR[7] #101800 "Crankcase pressure";
		Pa= PAR[8] #101800 "Crankcase pressure";
		wiebe_a= PAR[9]      #5 "Wiebe coeff. a";
		wiebe_m= PAR[10]	#2 "Wiebe coeff. m";
		alfa= PAR[11]	# Коэффициент избытка воздуха


		fp = FluidProperties([],[])

		
		T0 = fp.TG(PAR,12)+273.15
		MM = fp.MM(PAR,12)  #28.98/1000
		Cp = fp.Cp(PAR,12)         #1005
		R = fp.R(PAR,12)          #8.31441; 
		# print 
		# print 'test: -0.3'

		# print str(COMMON)
		time = COMMON.TIME

		eps = 1e-10			# точность определения 0
#		Pa=0.0
#    amplitude = 0.0;
#    w = 0.0;
#    dps = 0.0;
		start_burn = -1.0 #(start=-1);
		end_burn = -1.0  #(start=-1);
		burning = 0.0    #(start=false);
		# print 
		# print 'test: -0.1'

		
#    Vc = PAR[11]  #"Clearance volume";
#    Ap = PAR[12]  #"Piston area";
#    Vd = PAR[13]  #"Displaced volume";
#    crank_l  = PAR[14]  #"Crank length";
#    L_cylinder = PAR[15] #"Cylinder length";

#    U = 0.0 # "Total energy";
#    m = 0.0 #"Total mass";
		m_fuel_burnt = 0.0 #"Mass of fuel";
		m_fuel_start = 0.0 #"Start mass of fuel";

#    P = 0.0 #"Pressure";
#    T  = 0.0 #"Temperature";
#    mdot = 0.0#"Net mass flow";
#    q = 0.0 #"Net power";
#    H_flow_burn = 0.0 #"Power from burn";
#    V = 0.0 #"Chamber volume";
#    N = 1 #"Number of moles of gas";
#   A_chamber =1 #"Chamber area";
#    h_convection =1 #
		# print 
		# print 'test: -0.2'
	
		Ap = math.pi*(bore/2.0)**2;
		Vd = stroke*Ap;
		Vc = Vd/(comp_ratio - 1.0);
		crank_l = stroke/2.0;
# 
		# print 
		# print 'test: 0'

		P = V[1]
		
		T = V[2]
		der_T = A[2]
		
		spark = V[3]

		piston_s = X[4]
		piston_v = V[4]

		crank_phi = X[5]+0.0
		der_crank_phi = V[5]

		heatPort_T = V[6]
		Gc = V[7]

		m = V[8]
		der_m = A[8]

		heatPort_Q_flow  = V[9]
		intake_m_flow = V[10]
		
		
		start_burn = OLD [1]
		end_burn   = OLD [2]
		burning    = OLD [3]
		m_fuel_start = OLD [4]
#
		# print 'burning = ', burning
		# print 'end_burn = ', end_burn
		# print 
		# print 'test: 1'
#  //ChamberVolume
		L_cylinder = stroke*((1.0-cos(crank_phi))/2.0)

		# print 
		# print 'test: 1.01'

		
		V1 = Vc + Ap*L_cylinder;

		# print 
		# print 'test: 1.02'

		
		der_V = Ap * stroke*sin (crank_phi)*der_crank_phi/2.0

		# print 
		# print 'test: 1.1'

#  // Convection parameters
		A_chamber = 2.0*Ap + L_cylinder*math.pi*bore;

		# print 
		# print 'test: 1.2'

	
		eps_piston_v = piston_v
		if piston_v<0.0:
			kk = -1.0
		else:
			kk = 1.0
		if abs(piston_v)<eps:
			eps_piston_v = piston_v + eps*kk
		h_convection = 12.0 + 7.8*abs(eps_piston_v)**0.78;
		Gc_cylinder = A_chamber*h_convection;
		# print 
		# print 'test: 1.2.0'
		
		if (piston_v<0.0):
			# print 
			# print 'test: 1.2.1'

			derv_Gc = -A_chamber*7.8*(-eps_piston_v)**(0.78-1.0)*0.78
		else:
			derv_Gc = A_chamber*7.8*(eps_piston_v)**(0.78-1.0)*0.78
			
		if abs(piston_v)<eps:
			derv_Gc = 0.0
		# print 
		# print 'test: 1.3'

	
		N = m/MM;

		# print 
		# print 'test: 1.4'

		sign_der_T = 1.0
#		if (T+T0<eps):
#			T = eps-T0
#			der_T = 0.0
#			sign_der_T = 0.0
			
		H = Cp * (T + T0)
		U = m * (H - R*(T+T0))
#		der_U = der_m* (H - R*(T+T0))+m*(Cp-R)*der_T
		der_U = der_m* (-R*(T+T0))+m*(Cp-R/MM)*der_T
		dps = der_crank_phi;
	
#    q = intake.H_flow + exhaust.H_flow + heatPort.Q_flow;

		# print 
		# print 'test: 2'


#  algorithm
#		m_fuel_start = 0.0
#		m_fuel_start =m/afr
#    when start then
		if (abs(spark-1.0)<eps) & (abs(burning)<eps):
			start_burn = time
#			end_burn = time + (burn_duration/dps)
			end_burn = crank_phi + burn_duration
			amplitude = lhv*(m/(afr + 1))*2.0*dps/burn_duration
#			m_fuel_start =m/afr
			burning = 1.0
			if alfa>=1.0:
				m_fuel_start =m/(afr*alfa+1.0)
			else:
				m_fuel_start =m * alfa /(afr*alfa+1.0)
			
#			print 'burning = ', burning
#			print 'spark = ', spark
			
#			import msvcrt
#			ch = msvcrt.getch()

			
#    end when;
#    when time >= end_burn then
		df = 0.0*math.pi/180.0
		if (crank_phi  >= df+end_burn) & (abs(burning-1)<eps):
#		if (time  >= end_burn) & (abs(burning-1.0)<eps):
			burning = 0.0
#    end when;

		NEW[1] = start_burn
		NEW[2] = end_burn
		NEW[3] = burning
		NEW[4] = 	m_fuel_start


		# print 
		# print 'test: 3'

	
#  //Combustion
		der_m_fuel_burnt = 0.0
		if ((abs(burning-1.0)<eps)):
			end_burn_time = start_burn + (burn_duration/dps)
			t_burning = (end_burn_time - start_burn)
			loc_time = (time - start_burn)/t_burning
			expf = exp(-wiebe_a*((loc_time)**(wiebe_m+1.0)))
			m_fuel_burnt= m_fuel_start *(1.0 - expf);
#			der_m_fuel_burnt = wiebe_a /t_burning* ((loc_time)**wiebe_m) * expf
			der_m_fuel_burnt = m_fuel_start *wiebe_a *(wiebe_m+1.0)/t_burning* ((loc_time)**wiebe_m) * expf

			H_flow_burn = lhv*der_m_fuel_burnt;
		else:
			m_fuel_burnt = 0.0;
			H_flow_burn = 0.0;

		# print 
		# print 'test: 4'
	  
#    // First law of thermodynamics
#    eqFirstLaw = der_U -( q + H_flow_burn - P*der_V);
#		q = der_U -( H_flow_burn - P*der_V)
		q = der_U -( H_flow_burn - (P+Pa)*der_V)

	
#  equation
 	
		eq_heatPort_T = heatPort_T - T; #heatPort.T = medium.T;
		
#    // Ideal gas law
#		eqIdealGasLow = N*R*(T+T0)-P*V1;
		eqIdealGasLow = N*R*(T+T0)-(P+Pa)*V1;

		intake_H_flow= q - heatPort_Q_flow ;

#    // Conservation of mass
		eqM = der_m - intake_m_flow;
	
		eqGc = -Gc_cylinder + Gc

		crank_tau = 0.0;
		piston_f = -Ap*(P - Pcc);

		# print 
		# print 'test: 5'

		WRK[1] = m
		WRK[2] = der_m
		WRK[3] = V1
		WRK[4] = der_V
		WRK[5] = H
		WRK[6] = U
		WRK[7] = der_U
		# print 
		# print 'test: 5.5'
		WRK[8] = burning
		# print 
		# print 'test: 5.6'
		WRK[9] = m_fuel_burnt
		# print 
		# print 'test: 5.7'
		
		WRK[10] = der_m_fuel_burnt
		# print 
		# print 'test: 5.8'
		WRK[11] = H_flow_burn
		
		WRK[12] =eqIdealGasLow

		# print 
		# print 'test: 6'
		
# streams
		I [1] = intake_m_flow
		I [2] = intake_H_flow
#test
#		I [1] = V[1]
#		I [2] = V[2]

		I [3] = 0.0 #+ V[3]
		I [4] = piston_f #+ V[4]
		I [5] = 0.0 #+ V[5]
		I [6] = heatPort_Q_flow #+ V[6]
#		I [6] = V[6]
		I [7] = eqGc
#		I [7] = V[7]
		I [8] = eqM #+ V[8]
		I [9] = eq_heatPort_T
		I [10]= eqIdealGasLow #+ V[10]
			
		for i in xrange(3*Next**2):
			Y[i+1] = 0.0
	
		dyv = Next**2
		dya = 2*dyv

		
#		Y[1+Next*0+dyv]  = 1.0    				# test
		Y[10+Next*0+dyv] = 1.0					# intake_m_flow

#		Y[2+Next*1+dyv]  = 1.0    				# test
		Y[9+Next*1+dyv]  = -1.0    				# heatPort_Q_flow
#		Y[8+Next*1+dya]  = (Cp-R) * (T+T0)    	#  m'
#		Y[8+Next*1+dyv]  = der_T * (T+T0)  		  #  m
#		Y[2+Next*1+dyv]  = (Cp-R) * der_m *sign_der_T  	 #  T		
#		Y[2+Next*1+dya]  = (Cp-R) * m *sign_der_T    		#  T'
		Y[8+Next*1+dya]  = (-R) * (T+T0)    	#  m'
		Y[8+Next*1+dyv]  = der_T * (Cp-R/MM)  		  #  m
		Y[2+Next*1+dyv]  = (-R) * der_m *sign_der_T  	 #  T		
		Y[2+Next*1+dya]  = (Cp-R/MM) * m *sign_der_T    		#  T'
		Y[1+Next*1+dyv]  = der_V#1.0    				#  P
		Y[5+Next*1]  = (P+Pa)*Ap*stroke*der_crank_phi*cos(crank_phi)/2.0 #  crank_phi
		Y[5+Next*1+dyv]  = (P+Pa)*Ap*stroke*sin (crank_phi)/2.0    		#  der_crank_phi 
		
#		Y[3+Next*2+dyv]  = 1.0    				# test
		Y[3+Next*2]  = 0.0    				# 
		
#		Y[4+Next*3+dyv]  = 1.0    				# test
		Y[1+Next*3+dyv]  = -Ap    				# P

		Y[5+Next*4]  = 0.0    				# crank_phi
#		Y[5+Next*4+dyv]  = 1.0    				# test

#		Y[6+Next*5+dyv]  = 1.0    				# test
		Y[9+Next*5+dyv]  = 1.0    				# heatPort_Q_flow

		Y[7+Next*6+dyv]  = 1.0    				# Gc
		Y[4+Next*6+dyv]  = -derv_Gc    			# piston_v
#		Y[6+Next*6+dyv]  = 1.0    				# test

		
#		Y[8+Next*7+dyv]  = 1.0    				# test
		Y[8+Next*7+dya]  = 1.0    				# m'
		Y[10+Next*7+dyv]  = -1.0    			# intake_m_flow
		
#		Y[9+Next*8+dyv]  = 1.0    				# test
		Y[2+Next*8+dyv]  = -1.0    				# T
		Y[6+Next*8+dyv]  = 1.0    				# heatPort_T
		
#		Y[10+Next*9+dyv]  = 1.0    				# test
		Y[8+Next*9+dyv]  = R*(T+T0)/MM				# m
		Y[2+Next*9+dyv]  = m/MM*R  *sign_der_T  			# T
		Y[1+Next*9+dyv]  = -V1		   			# P
		
		Y[5+Next*9]  = -(P+Pa)*Ap*stroke*sin(crank_phi)/2.0		# crank_phi
	

		res = return_result(COMMON, I, Y, X, V, A, NEW, OLD, WRK)
		return res

		
	