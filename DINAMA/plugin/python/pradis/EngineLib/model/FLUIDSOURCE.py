# coding=Windows-1251
#HELP<model name="FluidSource" module="EngineLib" alias = "FLUIDS" ext="2" par="3" adr="2" ign ="3">   
#HELP	<description>
#HELP		<russian>
#HELP 		Источник жидкости 
#HELP		</russian>
#HELP		<english>The description of M3D image</english>
#HELP	</description>
#HELP	<nodelist>
#HELP		<node name="Out" type="EngineLib.ThermalFluid">
#HELP			<description>
#HELP				<russian>Выход</russian>
#HELP				<english>The description of M3D image</english>
#HELP			</description>
#HELP   	</node>
#HELP	</nodelist>
#HELP	<parameterlist>
#HELP		<parameter name="Pressure" type="real" default="101305.0">
#HELP			<description>
#HELP				<russian>Давление жидкости, Па</russian>
#HELP				<english>Inertia coefficient (mass)</english>
#HELP			</description>
#HELP		</parameter>
#HELP		<parameter name="Temperature" type="real" default="27.0">
#HELP			<description>
#HELP				<russian>Температура жидкости, гр.С</russian>
#HELP				<english>Inertia coefficient (mass)</english>
#HELP			</description>
#HELP		</parameter>
#HELP		<parameter name="k" type="real" default="1e6">
#HELP			<description>
#HELP				<russian>Коэффициент погрешности моделирования</russian>
#HELP				<english>Inertia coefficient (mass)</english>
#HELP			</description>
#HELP		</parameter>
#HELP	</parameterlist>
#HELP	<worklist>
#HELP	</worklist>
#HELP	<statelist>
#HELP	</statelist>
#HELP	<image2d icon = "EngineLib.FluidSource" symbol = ""/>	
#HELP</model> 

from pradis.ppl.model import *
#from PradisLog import *
from array import *

class FLUIDSOURCE (model):

	
	def Execute(COMMON, I, Y, X, V, A, PAR, NEW, OLD, WRK):
		if COMMON.NEWINT == 1:                       
#			pl = PradisLog()
			ERR = 0



			if ERR == 1:
				if COMMON.CODE < 100.:
					COMMON.CODE = 100.

				res = return_result(COMMON, I, Y, X, V, A, NEW, OLD, WRK)
				return res

		p = PAR[1]
		T = PAR[2]
		k = PAR[3]

		I[1]  =  -k*(V[1]-p)
		I[2]  =  -k*(V[2]-T)
#		I[3]  =  -k*(V[3]-H)

		for i in xrange(2**2):
			Y[i+1] = 0.0
		
		Y[1]  =  -k
		Y[4]  =  -k
#		Y[9]  =  -k

		res = return_result(COMMON, I, Y, X, V, A, NEW, OLD, WRK)
		return res

