# coding=Windows-1251
#HELP<model name="Convection" module="EngineLib" ext="3" par="1" adr="2" ign ="3">   
#HELP	<description>
#HELP		<russian>
#HELP 		Модель конвективного теплообмена
#HELP		</russian>
#HELP		<english>The description of M3D image</english>
#HELP	</description>
#HELP	<nodelist>
#HELP		<node name="Gc" type="base.DOF1">
#HELP			<description>
#HELP				<russian>Сигнал конвективной теплопроводности</russian>
#HELP				<english>The description of M3D image</english>
#HELP			</description>
#HELP   	</node>
#HELP		<node name="solid" type="base.DOF1">
#HELP			<description>
#HELP				<russian>Сторона твердого тела</russian>
#HELP				<english>The description of M3D image</english>
#HELP			</description>
#HELP   	</node>
#HELP		<node name="fluid" type="base.DOF1">
#HELP			<description>
#HELP				<russian>Сторона жидкого тела</russian>
#HELP				<english>The description of M3D image</english>
#HELP			</description>
#HELP   	</node>
#HELP	</nodelist>
#HELP	<parameterlist>
#HELP		<parameter name="K" type="real" default="1.0">
#HELP			<description>
#HELP				<russian>Коэффициент пропорциональности сигнала теплопроводности</russian>
#HELP				<english>Inertia coefficient (mass)</english>
#HELP			</description>
#HELP		</parameter>
#HELP	</parameterlist>
#HELP	<worklist>
#HELP	</worklist>
#HELP	<statelist>
#HELP	</statelist>
#HELP	<image2d icon = "EngineLib.Convection" symbol = ""/>	
#HELP</model> 

from pradis.ppl.model import *
#from PradisLog import *
from array import *

class CONVECTION (model):

	
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

		h = V[1]
		Tw = V[2] # температора твердого тела
		T = V[3]   # температора жидкого тела
		
		q = h * (T-Tw)
				
		I[1]  =  0.0
		I[2]  =  q
		I[3]  =  -q

		
		Y[1]  =  0.0
		Y[2]  =  0.0
		Y[3]  =  0.0

		Y[4]  =  0.0
		Y[5]  =  h
		Y[6]  =  -h

		Y[7]  =  -Y[4]
		Y[8]  =  -h
		Y[9]  =  h

		res = return_result(COMMON, I, Y, X, V, A, NEW, OLD, WRK)
		return res

