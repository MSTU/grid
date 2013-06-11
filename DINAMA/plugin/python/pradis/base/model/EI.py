# coding=Windows-1251
#HELP<model name="EI" module="base" ext="2" ent = "1" par="1" adr="2" ign = "3">   
#HELP	<description>
#HELP		<russian>
#HELP 		Идеальный источник ЭДС
#HELP		</russian>
#HELP		<english>The description of M3D image</english>
#HELP	</description>
#HELP	<nodelist>
#HELP		<node name="Node1" type="DOF1"></node>
#HELP		<node name="Node2" type="DOF2"></node>
#HELP	</nodelist>
#HELP	<parameterlist>
#HELP		<parameter name="E" type="real" default="1.0">
#HELP			<description>
#HELP				<russian>Значение ЭДС</russian>
#HELP				<english>Inertia coefficient (mass)</english>
#HELP			</description>
#HELP		</parameter>
#HELP	</parameterlist>
#HELP	<worklist>
#HELP	</worklist>
#HELP	<statelist>
#HELP	</statelist>
#HELP	<image2d icon = "base.EI"/>	
#HELP</model> 

from pradis.ppl.model import *
from PradisLog import *
from array import *

class EI (model):

	
	def Execute(COMMON, I, Y, X, V, A, PAR, NEW, OLD, WRK):


		I[1]  =  V[3]
		I[2]  =  - V[3]
		I[3]  =  V[1]-V[2]-PAR[1]

		Y[1]  =  0.
		Y[2]  =  0.  
		Y[3]  =  1.0  
		Y[4]  =  0.  
		Y[5]  =  0.
		Y[6]  =  -1.0  
		Y[7]  =  1.  
		Y[8]  =  -1.  
		Y[9]  =  0.

		res = return_result(COMMON, I, Y, X, V, A, NEW, OLD, WRK)
		return res

