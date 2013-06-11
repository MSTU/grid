# coding=Windows-1251
#HELP<ovp name="LinesIntersection" module="d3" alias="" priority="5" out="3" par="8" vpr="0" vps="0" wrs="0" wrk="0" wrp="0" sys="12">
#HELP	<description>
#HELP		<russian>Программа для определения пересечений линий</russian>
#HELP		<english>Subroutine for line intersection definition</english>
#HELP	</description>
#HELP	<nodelist>
#HELP		<node name="Node1OfLine1" type="base.Point2d">
#HELP			<description>
#HELP				<russian>Узел 1 отрезка 1</russian>
#HELP				<english>Node 1 of line 1</english>
#HELP			</description>
#HELP		</node>
#HELP		<node name="Node2OfLine1" type="base.Point2d">
#HELP			<description>
#HELP				<russian>Узел 2 отрезка 1</russian>
#HELP				<english>Node 2 of line 1</english>
#HELP			</description>
#HELP		</node>
#HELP		<node name="Node2OfLine2" type="base.Point2d">
#HELP			<description>
#HELP				<russian>Узел 2 отрезка 2</russian>
#HELP				<english>Node 2 of line 2</english>
#HELP			</description>
#HELP		</node>
#HELP	</nodelist>
#HELP	<parameterlist>
#HELP		<parameter name="Point1ofLine1" type="base.pXY" default="0.,0.">
#HELP			<description>
#HELP				<russian>Начальные координаты узла 1 отрезка 1</russian>
#HELP				<english>Initial coordinates of point 1 of line1</english>
#HELP			</description>
#HELP		</parameter>
#HELP		<parameter name="Point2ofLine1" type="base.pXY" default="1.,0.">
#HELP			<description>
#HELP				<russian>Начальные координаты узла 2 отрезка 1</russian>
#HELP				<english>Initial coordinates of point 2 of line1</english>
#HELP			</description>
#HELP		</parameter>
#HELP		<parameter name="Point1ofLine2" type="base.pXY" default="0.,0.">
#HELP			<description>
#HELP				<russian>Начальные координаты узла 1 отрезка 2</russian>
#HELP				<english>Initial coordinates of point 1 of line2</english>
#HELP			</description>
#HELP		</parameter>
#HELP		<parameter name="Point2ofLine2" type="base.pXY" default="0.,1.">
#HELP			<description>
#HELP				<russian>Начальные координаты узла 2 отрезка 2</russian>
#HELP				<english>Initial coordinates of point 2 of line2</english>
#HELP			</description>
#HELP		</parameter>
#HELP	</parameterlist>
#HELP	<image2d icon = "d3.LinesIntersection" symbol = "    .PortSym 40 20 1 0:
#HELP    .PortSym 40 60 2 0:
#HELP    .PortSym 40 100 3 0:
#HELP    .PortSym 40 140 4 0:
#HELP"/>
#HELP	<worklist>
#HELP	</worklist>
#HELP</ovp>



from pradis.ppl.ovp import *
import math

class LinesIntersection(ovp):
	def Execute(COMMON, XOUT, PAR, WRK, DOF):
		x1 = DOF[1]+PAR[1]
		y1 = DOF[2]+PAR[2]
		x2 = DOF[4]+PAR[3]
		y2 = DOF[5]+PAR[4]
		x3 = DOF[7]+PAR[5]
		y3 = DOF[8]+PAR[6]
		x4 = DOF[10]+PAR[7]
		y4 = DOF[11]+PAR[8]
		
		d = (x2-x1)*(y4-y3)-(x4-x3)*(y2-y1)
		d1= (x3-x1)*(y4-y3)-(x4-x3)*(y3-y1)
		d2 = (x2-x1)*(y3-y1)-(x3-x1)*(y2-y1)
		
		if (math.abs(d)<1e-8):
			XOUT[1] =0.0
			XOUT[2] =0.0
			XOUT[3] =0.0
			res = return_result(COMMON, XOUT, WRK)
			return res
		
		t1 = d1/d
		t2 = d2/d

#check!	
		f1 = (x2-x1)*t1+(x4-x3)*t2- (x3-x1)
		f2 = (y2-y1)*t1+(y4-y3)*t2- (y3-y1)
		
		if (math.abs(f1)>1e-8 | math.abs(f2)>1e-5):
			print 'Wrong linear system calculation'
			
		if (t1>0.0):
			r1 = t1-1.0
		else:
			r1 = - t1
		
		if (t2>0.0):
			r2 = t2-1.0
		else:
			r2 = - t2
		
		r = r1 + r2

		if (r1<WRK[1]):
			WRK[1] = r1		
		if (r2<WRK[2]):
			WRK[2] = r2		
		
		XOUT[1] =r
		XOUT[2] =r1
		XOUT[3] =r2
	
		res = return_result(COMMON, XOUT, WRK)
		return res

