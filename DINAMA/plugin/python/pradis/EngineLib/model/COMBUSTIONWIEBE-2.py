# coding=Windows-1251
#HELP<model name="CombustionWiebe" module="EngineLib" alias = "COMBUS" vpr="1" ext="14" par="0" adr="2" ign ="3">   
#HELP	<description>
#HELP		<russian>
#HELP 		Камера сгорания на основе закона Вибе 
#HELP		</russian>
#HELP		<english>The description of M3D image</english>
#HELP	</description>
#HELP	<nodelist>
#HELP		<node name="Intake" type="EngineLib.ThermalFluid">
#HELP			<description>
#HELP				<russian>Вход клапана</russian>
#HELP				<english>The description of M3D image</english>
#HELP			</description>
#HELP   	</node>
#HELP		<node name="Exhaust" type="EngineLib.ThermalFluid">
#HELP			<description>
#HELP				<russian>Выход клапана</russian>
#HELP				<english>The description of M3D image</english>
#HELP			</description>
#HELP   	</node>
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
#HELP		<node name="heatPort" type="EngineLib.HeatPort">
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
#HELP	<image2d icon = "EngineLib.CombustionWiebe" symbol = ""/>	
#HELP</model> 

from pradis.ppl.model import *
#from PradisLog import *
from array import *

class COMBUSTIONWIEBE (model):

	
	def Execute(COMMON, I, Y, X, V, A, PAR, NEW, OLD, WRK):
		if COMMON.NEWINT == 1:                       
#			pl = PradisLog()
			ERR = 0


			if ERR == 1:
				if COMMON.CODE < 100.:
					COMMON.CODE = 100.

				res = return_result(COMMON, I, Y, X, V, A, NEW, OLD, WRK)
				return res

		Next = 14
		
		spark = V[10]		
		v_piston = V[11]
		v_crank = V[12]
		T_heat = V[13]
		
		qfIntake = V[7]-V[1]
		qTIntake = V[8]-V[2]
		qHIntake = V[9]-V[3]
		
		qfExhaust = V[7]-V[4]
		qTExhaust = V[8]-V[5]
		qHExhaust = V[9]-V[6]

		qfChamber = -V[7]
		qTChamber = -V[8]
		qHChamber = -V[9]
		
		f_piston = 0.0
		m_crank = 0.0
		q_heat = - T_heat
		Gc = 0.0
		

		I[1]  =  -qfIntake
		I[2]  =  -qTIntake
		I[3]  =  -qHIntake

		I[4]  =  -qfExhaust
		I[5]  =  -qTExhaust
		I[6]  =  -qHExhaust

		I[7]  =  qfChamber
		I[8]  =  qfChamber
		I[9]  =  qfChamber

		I[10]  =  0.0
		I[11]  =  f_piston
		I[12]  =  m_crank
		I[13]  =  q_heat
		I[14]  =  Gc

		
		
		for i in xrange(Next**2):
			Y[i+1] = 0.0
		
#	intake		
		Y[1]  =  1.0
		Y[7]  =  -1.0
		
		Y[2+Next*1]  =  1.0
		Y[8+Next*1]  =  -1.0
		
		Y[3+Next*2]  =  1.0
		Y[9+Next*2]  =  -1.0

#	exhaust		
		Y[4+Next*3]  =  1.0
		Y[7+Next*3]  =  -1.0
		
		Y[5+Next*4]  =  1.0
		Y[8+Next*4]  =  -1.0
		
		Y[6+Next*5]  =  1.0
		Y[9+Next*5]  =  -1.0

#	chamber		
		Y[7+Next*6]  =  -1.0
		
		Y[8+Next*7]  =  -1.0
		
		Y[9+Next*8]  =  -1.0

#	piston		
		Y[11+Next*10]  =  1.0
#	crank		
		Y[12+Next*11]  =  1.0
#	heat		
		Y[13+Next*12]  =  -1.0
#	Gc		
		Y[14+Next*13]  =  -1.0



		res = return_result(COMMON, I, Y, X, V, A, NEW, OLD, WRK)
		return res

		
    bore = PAR[1]
    stroke = PAR[2]
    conrod  = PAR[3]
    comp_ratio= PAR[4] #9.5 "Compression ratio";
    lhv = PAR[5] #44e+6      "Fuel lower heating value";
    afr=PAR[6]   #14.7 "Air/Fuel Ratio";
    burn_duration=PAR[7] #60       "Duration of combustion";
    Pressure Pcc= PAR[8] #101800 "Crankcase pressure";
    wiebe_a= PAR[9]      #5 "Wiebe coeff. a";
    wiebe_m= PAR[10]	#2 "Wiebe coeff. m";

    amplitude = 0.0;
    w = 0.0;
    dps = 0.0;
    start_burn = -1 #(start=-1);
    end_burn = -1  #(start=-1);
    burning = 0    #(start=false);

#    Vc = PAR[11]  #"Clearance volume";
#    Ap = PAR[12]  #"Piston area";
#    Vd = PAR[13]  #"Displaced volume";
#    crank_l  = PAR[14]  #"Crank length";
    L_cylinder = PAR[15] #"Cylinder length";

    U = 0.0 # "Total energy";
    m = 0.0 #"Total mass";
    m_fuel_burnt = 0.0 #"Mass of fuel";
    m_fuel_start = 0.0 #"Start mass of fuel";

    P = 0.0 #"Pressure";
    T  = 0.0 #"Temperature";
    mdot = 0.0#"Net mass flow";
    q = 0.0 #"Net power";
    H_flow_burn = 0.0 #"Power from burn";
    V = 0.0 #"Chamber volume";
    N = 1 #"Number of moles of gas";
    A_chamber =1 #"Chamber area";
    h_convection =1 #
    R = 8.31441; 

    Vc = Vd/(comp_ratio - 1.0);
    Ap = math.pi*(bore/2.0)**2;
    Vd = stroke*Ap;
    crank_l = stroke/2.0;
###	
	intake_p = V[2]
	medium_T = V[7]
	piston_s = X[]
	piston_v = V[]
	crank_phi = X[]
	der_crank_phi = V[]
	
	U = X[]
	der_U = V[]
	m = X[]
	der_m = V[]
###
   P = intake_p;
    T = medium_T;
	medium_MM = 
	
	
	
  //ChamberVolume
    L_cylinder = stroke*((1-cos(crank_phi))/2.0);
    V = Vc + Ap*L_cylinder;

  // Convection parameters
    A_chamber = 2*Ap + L_cylinder*math.pi*bore;
    h_convection = 12.0 + 7.8*abs(piston_v)**0.78;
    Gc_cylinder = A_chamber*h_convection;
 	
    N = m/medium.MM;

	
	
    mdot = intake.m_flow + exhaust.m_flow;
#    q = intake.H_flow + exhaust.H_flow + heatPort.Q_flow;
  //Combustion
    if (burning):
      m_fuel_burnt= m_fuel_start *(1 - exp(-wiebe_a*((time - start_burn)/
					(end_burn - start_burn))^(wiebe_m+1)));
		der_m_fuel_burnt = 
      H_flow_burn = lhv*der_m_fuel_burnt;
    else:
      m_fuel_burnt = 0;
      H_flow_burn = 0.0;

    // First law of thermodynamics
#    eqFirstLaw = der_U -( q + H_flow_burn - P*der_V);
	q = der_U -( H_flow_burn - P*der_V)

	
  equation
	eq_medium_p = intake_p - exhaust_p#    intake.p = medium.p;
	eq_medium_h = intake_h - exhaust_h#    intake.h = medium.h;
#    intake.Xi = medium.Xi;
#    exhaust.p = intake.p;
#    exhaust.h = intake.h;
#    exhaust.Xi = intake.Xi;
	
    eq_heatPort_T = heatPort.T - medium.T; #heatPort.T = medium.T;
		
    // Ideal gas law
    eqIdealGasLow = N*R*T-P*V;

    heatPort.Q_flow = q - intake.H_flow + exhaust.H_flow ;

    eqU = m*medium.u-U;

    // Conservation of mass
    eqM = der_m - mdot;
	
    

    
    dps = der_crank_phi*180/math.pi;

    crank_tau = 0.0;
    piston_f = -Ap*(P - Pcc);
	
