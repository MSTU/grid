# coding=Windows-1251
#HELP<model name="NOxV1" module="EngineLib" alias = "NOXV1" ext="3" par="1" vpr = "1" adr="2" ign ="3" wrk = "0">   
#HELP	<description>
#HELP		<russian>
#HELP 		Расчет концентрации NO по эмпирической формуле 
#HELP		</russian>
#HELP		<english>The description of M3D image</english>
#HELP	</description>
#HELP	<nodelist>
#HELP		<node name="In" type="EngineLib.ThermalFluid">
#HELP			<description>
#HELP				<russian>Вход</russian>
#HELP				<english>The description of M3D image</english>
#HELP			</description>
#HELP   	</node>
#HELP		<node name="NO" type="base.DOF1">
#HELP			<description>
#HELP				<russian>Концентрация NO, ppm/10^6</russian>
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
#HELP		<parameter name="K1" type="real" default="36656">
#HELP			<description>
#HELP				<russian>Показатель экспоненты</russian>
#HELP				<english>Inertia coefficient (mass)</english>
#HELP			</description>
#HELP		</parameter>
#HELP		<parameter name="K2" type="real" default="4.7e9">
#HELP			<description>
#HELP				<russian>Множитель экспоненты</russian>
#HELP				<english>Inertia coefficient (mass)</english>
#HELP			</description>
#HELP		</parameter>
#HELP	</parameterlist>
#HELP	<worklist>
#HELP	</worklist>
#HELP	<statelist>
#HELP	</statelist>
#HELP	<image2d icon = "EngineLib.NOxV1" symbol = ""/>	
#HELP</model> 

from pradis.ppl.model import *
#from PradisLog import *
from array import *
from  pradis.EngineLib.FluidProperties import *
from math import *

class NOXV1(model):

		
		
	
	def Execute(COMMON, I, Y, X, V, A, PAR, NEW, OLD, WRK):
		if COMMON.NEWINT == 1:                       
#			pl = PradisLog()
			ERR = 0



			if ERR == 1:
				if COMMON.CODE < 100.:
					COMMON.CODE = 100.

				res = return_result(COMMON, I, Y, X, V, A, NEW, OLD, WRK)
				return res

		
		Pa= PAR[1] #101000 "Reference pressure";
		K1= PAR[2] #101000 "Reference pressure";
		K2= PAR[3]

		eps = 1e-20
		
		Pin = V[1]+Pa
		Tin = V[2]+273.15
		
		NO	= V[3]

#		print 'A=', V[5]

		if Tin < eps:
			Tin = eps
		
		ppm=K2*exp (-K1/Tin)*1e-6
		q=ppm-NO
		derT_q = K2*K1/ (Tin**2)*exp (-K1/Tin) * 1e-6

		I[1]  =  0.0
		I[2]  =  0.0
		I[3]  =  q
		
		for i in xrange(3**2):
			Y[i+1] = 0.0
		
		#I[3]
		Y[2+2*3]  =  derT_q
		Y[3+2*3]  =  -1.0

		
		res = return_result(COMMON, I, Y, X, V, A, NEW, OLD, WRK)
		return res
