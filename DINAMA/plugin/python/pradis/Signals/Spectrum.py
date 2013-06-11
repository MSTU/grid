# -*- coding: cp1251 -*-
from scipy.fftpack import *
from string import *
from scipy import interpolate
import scipy
import math
import af
import misc
import os
from tools import*
class Spectrum:

	def __init__ (self, nl, pl, desc=misc.default):
		 
#------------------------------------getting variables--------------------------------------		
		Scheme=pl[0]
		Dat=pl[1]
		Output_Signals_List=pl[2]
		Frequency=pl[3]
#------------------------------------main function-----------------------------------
		if Scheme!='':
			Dat=Simulation_Scheme(Scheme)
		sc = af.SolverContext (Dat)																			#������������� ��������� ��������
		dc = af.OutVariableContext (sc)																		#������������� ��������� ����
			
		Output_Signals_Numbers=Getting_List_ID(Output_Signals_List,sc,dc)									#��������� ������ ID ����
		Input_Data=Formation_Array_Data(sc,dc,Output_Signals_Numbers)										#��������� ������ �� ID ���� � ��������� ����� �� DAT �����
		MaxFrequency=Calculation_MaxFrequency(Frequency)													#���������� ������������ �������(���������� �� � ������� ������� ������)
		Discretization=MaxFrequency*16*math.ceil(Input_Data[-1,-1])											#���������� ����� ����� ������������� 
		Interpolated_Data=Interpolate_Data(Input_Data,Discretization)										#���������� ������������ ������  �� ����� ����� �������������
		Spectrum=Amplitude_Spectrum(Interpolated_Data[0:-1])												#��������� ������� ������� ��� ����������������� ��������
		print 'sssss'
		Output_List=scipy.zeros((len(Spectrum)*2+1,MaxFrequency*math.ceil(Input_Data[-1,-1])), float)		#������������ ��������� ������ ��� ������ � ���� *.hst

		for k in range(len(Spectrum)):
			Output_List[k]=Spectrum[k,:MaxFrequency*math.ceil(Input_Data[-1,-1])]							#������� ������������ ��������� �� ������� ��������
			Output_List[k+len(Spectrum)]=Spectrum[k,:MaxFrequency*math.ceil(Input_Data[-1,-1])]**2			#��������� ��������� ��������(��������� �������)
		h=0
		while h<MaxFrequency*math.ceil(Input_Data[-1,-1]):													
			Output_List[-1,h]=h/Input_Data[-1,-1]															#��������� ��� ������
			h+=1

		for h in range(len(Output_Signals_List)):															#�������� ������ ���� �������� ����������
			Output_Signals_List+=["PSD."+Output_Signals_List[h]]
			Output_Signals_List[h]="Spectrum."+Output_Signals_List[h]
		Output_Signals_List=["Frequency"]+Output_Signals_List
	
		writeFile (Output_List,Output_Signals_List,desc)													#����� ������� ������ ����������� � ����
		
		misc.SetSolver ("")																					#����� ������ ��������� � �������������
		misc.SetPost(os.getenv("DINSYS")+"\dinama\post\Postprocessor")										#����� ������ ��������� � �������������
		misc.SetPostFile(desc+".hst")																		#����� ������ ��������� � �������������