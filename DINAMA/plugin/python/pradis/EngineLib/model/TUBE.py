# coding=Windows-1251
#HELP<model name="Tube" module="EngineLib" alias="TUBE" ext="4" par="1" vpr = "1" adr="2" ign ="3">   
#HELP	<description>
#HELP		<russian>
#HELP 		Клапан 
#HELP		</russian>
#HELP		<english>The description of M3D image</english>
#HELP	</description>
#HELP	<nodelist>
#HELP		<node name="In" type="EngineLib.ThermalFluid">
#HELP			<description>
#HELP				<russian>Вход в канал</russian>
#HELP				<english>The description of M3D image</english>
#HELP			</description>
#HELP   	</node>
#HELP		<node name="Out" type="EngineLib.ThermalFluid">
#HELP			<description>
#HELP				<russian>Выход из канала</russian>
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
#HELP	<image2d icon = "EngineLib.Tube" symbol = ""/>	
#HELP</model> 

from pradis.ppl.model import *
#from PradisLog import *
from array import *

class TUBE (model):

	
	def Execute(COMMON, I, Y, X, V, A, PAR, NEW, OLD, WRK):
		if COMMON.NEWINT == 1:                       
#			pl = PradisLog()
			ERR = 0



			if ERR == 1:
				if COMMON.CODE < 100.:
					COMMON.CODE = 100.

				res = return_result(COMMON, I, Y, X, V, A, NEW, OLD, WRK)
				return res

		qF = V[3]-V[1]
		qT = V[4]-V[2]
				
		I[1]  =  -qF
		I[2]  =  -qT
		I[3]  =  - I[1]
		I[4]  =  - I[2]

		for i in xrange(4**2):
			Y[i+1] = 0.0
		
		Y[1]  =  1.0
		Y[3]  =  -1.0
		
		Y[2+1*4]  =  1.0
		Y[4+1*4]  =  -1.0
				
		Y[1+2*4]  =  -1.0
		Y[3+2*4]  =  1.0
		
		Y[2+3*4]  =  -1.0
		Y[4+3*4]  =  1.0
		

		res = return_result(COMMON, I, Y, X, V, A, NEW, OLD, WRK)
		return res

