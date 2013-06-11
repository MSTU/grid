# coding=Windows-1251
#HELP<model name="ThermalConductor" module="EngineLib" ext="2" par="1" adr="2" ign ="3">   
#HELP	<description>
#HELP		<russian>
#HELP 		Модель теплообмена путем теплопроводности. 
#HELP		</russian>
#HELP		<english>The description of M3D image</english>
#HELP	</description>
#HELP	<nodelist>
#HELP		<node name="A" type="base.DOF1">
#HELP			<description>
#HELP				<russian>Сторона А</russian>
#HELP				<english>The description of M3D image</english>
#HELP			</description>
#HELP   	</node>
#HELP		<node name="B" type="base.DOF1">
#HELP			<description>
#HELP				<russian>Сторона B</russian>
#HELP				<english>The description of M3D image</english>
#HELP			</description>
#HELP   	</node>
#HELP	</nodelist>
#HELP	<parameterlist>
#HELP		<parameter name="G" type="base.real" default="">
#HELP			<description>
#HELP				<russian>Теплопроводность материала (Дж/(кг*К))</russian>
#HELP				<english>Inertia coefficient (mass)</english>
#HELP			</description>
#HELP		</parameter>
#HELP	</parameterlist>
#HELP	<worklist>
#HELP	</worklist>
#HELP	<statelist>
#HELP	</statelist>
#HELP	<image2d icon = "EngineLib.ThermalConductor" symbol = ""/>	
#HELP</model> 

from pradis.ppl.model import *
#from PradisLog import *
from array import *

class THERMALCONDUCTOR (model):

	
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

		k = PAR[1]
		Tw = V[1] # температора твердого тела
		T = V[2]   # температора жидкого тела
		
#		print 'k = ', k
#		print 'Tw = ', Tw
#		print 'T = ', T
		
		
		q = k * (T-Tw)

		I[1]  =  q
		I[2]  =  -q

		
		Y[1]  =  -k
		Y[2]  =  k
		Y[3]  =  k
		Y[4]  =  -k

		res = return_result(COMMON, I, Y, X, V, A, NEW, OLD, WRK)
		return res

