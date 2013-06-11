# coding=Windows-1251
#HELP<model name="Pipe" module="EngineLib" ext="5" par="0" adr="2" ign ="3">   
#HELP	<description>
#HELP		<russian>
#HELP 		Участок трубопровода 
#HELP		</russian>
#HELP		<english>The description of M3D image</english>
#HELP	</description>
#HELP	<nodelist>
#HELP		<node name="A" type="EngineLib.ThermalFluid">
#HELP			<description>
#HELP				<russian>Вход А</russian>
#HELP				<english>The description of M3D image</english>
#HELP			</description>
#HELP   	</node>
#HELP		<node name="B" type="EngineLib.ThermalFluid">
#HELP			<description>
#HELP				<russian>Выход B</russian>
#HELP				<english>The description of M3D image</english>
#HELP			</description>
#HELP   	</node>
#HELP		<node name="heat" type="base.DOF1">
#HELP			<description>
#HELP				<russian>Тепло от трубопровода</russian>
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
#HELP	<image2d icon = "EngineLib.Pipe" symbol = ""/>	
#HELP</model> 

from pradis.ppl.model import *
#from PradisLog import *
from array import *

class Pipe (model):

	
	def Execute(COMMON, I, Y, X, V, A, PAR, NEW, OLD, WRK):
		if COMMON.NEWINT == 1:                       
#			pl = PradisLog()
			ERR = 0


			if ERR == 1:
				if COMMON.CODE < 100.:
					COMMON.CODE = 100.

				res = return_result(COMMON, I, Y, X, V, A, NEW, OLD, WRK)
				return res



		qF = V[4]-V[1]
		qT = V[5]-V[2]
				
		I[1]  =  -qF
		I[2]  =  -qT
		I[4]  =  - I[1]
		I[5]  =  - I[2]
		I[7]  =  0.0

		for i in xrange(5**2):
			Y[i+1] = 0.0
		
		Y[1]  =  1.0
		Y[3]  =  -1.0
		
		Y[2+1*5]  =  1.0
		Y[4+1*5]  =  -1.0
		
		
		Y[1+2*5]  =  -1.0
		Y[3+2*5]  =  1.0
		
		Y[2+3*5]  =  -1.0
		Y[4+3*5]  =  1.0
		
		
		Y[25]  =  0.0

		res = return_result(COMMON, I, Y, X, V, A, NEW, OLD, WRK)
		return res

