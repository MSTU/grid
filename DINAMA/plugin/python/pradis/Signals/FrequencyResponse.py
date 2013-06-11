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
class FrequencyResponse:

	def __init__ (self, nl, pl, desc=misc.default):
		 
#------------------------------------getting variables--------------------------------------		
		Scheme=pl[0]
		Dat=pl[1]
		Input_Signal=pl[2]
		Output_Signals_List=pl[3]
		Frequency=pl[4]
		eps=pl[5]
#------------------------------------main function-----------------------------------
		if Scheme!='':
			Dat=Simulation_Scheme(Scheme)
		print 'dddd'
		sc = af.SolverContext (Dat)																			#������������� ��������� ��������
		dc = af.OutVariableContext (sc)																		#������������� ��������� ����
		Signals_List=Output_Signals_List+[Input_Signal]
		Signals_Numbers=Getting_List_ID(Signals_List,sc,dc)													#��������� ������ ID ����
		Input_Data=Formation_Array_Data(sc,dc,Signals_Numbers)												#��������� ������ �� ID ���� � ��������� ����� �� DAT �����

		MaxFrequency=Calculation_MaxFrequency(Frequency)													#���������� ������������ �������(���������� �� � ������� ������� ������)
		Discretization=MaxFrequency*16*math.ceil(Input_Data[-1,-1])											#���������� ����� ����� ������������� 
		Interpolated_Data=Interpolate_Data(Input_Data,Discretization)										#���������� ������������ ������  �� ����� ����� �������������
		Spectrum_Amplitude=Amplitude_Spectrum(Interpolated_Data[0:-1])										#��������� ������� ������� ��� ����������������� ��������
		print 'dddd'
		Spectrum_Frequency=Frequency_Spectrum(Interpolated_Data[0:-1])
		Length_Signals_List=len(Output_Signals_List)
		Output_List=list(list() for k in range(Length_Signals_List*3+1))									#������������ ��������� ������ ��� ������ � ���� *.hst
		h=0
		while h<MaxFrequency*Input_Data[-1,-1]:																#������� ������������ ��������� �� ������� ��������
			if Spectrum_Amplitude[-1,h]>eps:
				for k in range(len(Output_Signals_List)):
					Output_List[k]+=[Spectrum_Amplitude[k,h]/Spectrum_Amplitude[-1,h]]						#���������� ��������� ������� ��������� � ��������
					Output_List[k+Length_Signals_List]+=[Spectrum_Frequency[k,h]-Spectrum_Frequency[-1,h]]
					Output_List[k+Length_Signals_List*2]+=[math.degrees(Spectrum_Frequency[k,h]-Spectrum_Frequency[-1,h])]
				Output_List[-1]+=[h/Input_Data[-1,-1]]														#��������� ��� ������
			h+=1

		Named_List=["PhaseResponce_in_Radians.","PhaseResponce_in_Degrees."] 
		Len_Signals_List=len(Output_Signals_List)															#���������� ����� ������ ��������
		for k in Named_List:																				#���� �� ���������� � ����� �������
			h=0
			while h <Len_Signals_List:																		#���� �� ������ ��������
				Output_Signals_List+=[k+Output_Signals_List[h]]															#���������� �� ���� ������ �������� ���������
				h+=1	
		h=0
		while h <Len_Signals_List:																			#���������� ���������
			Output_Signals_List[h]="FrequencyResponce."+Output_Signals_List[h]
			h+=1
		Output_Signals_List=["Frequency"]+Output_Signals_List
		writeFile (Output_List,Output_Signals_List,desc)													#����� ������� ������ ����������� � ����
		
		misc.SetSolver ("")																					#����� ������ ��������� � �������������
		misc.SetPost(os.getenv("DINSYS")+"\dinama\post\Postprocessor")										#����� ������ ��������� � �������������
		misc.SetPostFile(desc+".hst")																		#����� ������ ��������� � �������������