# coding=Windows-1251
#HELP<model name="HeatCapacitor" module="EngineLib" ext="1" par="1" adr="3" ign ="0">   
#HELP	<description>
#HELP		<russian>
#HELP 		Модель теплоемкости. 
#HELP		</russian>
#HELP		<english>The description of M3D image</english>
#HELP	</description>
#HELP	<nodelist>
#HELP		<node name="A" type="base.DOF1">
#HELP			<description>
#HELP				<russian>Тело</russian>
#HELP				<english>The description of M3D image</english>
#HELP			</description>
#HELP   	</node>
#HELP	</nodelist>
#HELP	<parameterlist>
#HELP		<parameter name="С" type="base.real" default="">
#HELP			<description>
#HELP				<russian>Удельная теплоемкость [Дж/(кг*К)]</russian>
#HELP				<english>Inertia coefficient (mass)</english>
#HELP			</description>
#HELP		</parameter>
#HELP	</parameterlist>
#HELP	<worklist>
#HELP	</worklist>
#HELP	<statelist>
#HELP	</statelist>
#HELP	<image2d icon = "EngineLib.HeatCapacitor" symbol = ""/>	
#HELP</model> 

from pradis.ppl.model import *
#from PradisLog import *
from array import *

class HEATCAPACITOR (model):

	
	def Execute(COMMON, I, Y, X, V, A, PAR, NEW, OLD, WRK):
		if COMMON.NEWINT == 1:                       
#			pl = PradisLog()
			ERR = 0

			if PAR[1] < 0.:
				ERR = 1
				if COMMON.SYSPRN > 0.:
					a = array ('d', [1., 0., 1., PAR[1]])
#					pl.perr (1003, 4, a.buffer_info()[0])


			if ERR == 1:
				if COMMON.CODE < 100.:
					COMMON.CODE = 100.

				res = return_result(COMMON, I, Y, X, V, A, NEW, OLD, WRK)
				return res

		C = PAR[1]
				
		I[1]  =  C * A[1]

		for i in xrange(1**2):
			Y[i+1] = 0.0
		
		Y[1]  =  C
		

		res = return_result(COMMON, I, Y, X, V, A, NEW, OLD, WRK)
		return res

