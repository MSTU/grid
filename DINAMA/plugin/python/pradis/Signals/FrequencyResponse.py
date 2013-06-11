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
		sc = af.SolverContext (Dat)																			#инициализация контекста решателя
		dc = af.OutVariableContext (sc)																		#инициализация контекста ПРВП
		Signals_List=Output_Signals_List+[Input_Signal]
		Signals_Numbers=Getting_List_ID(Signals_List,sc,dc)													#получение списка ID ПРВП
		Input_Data=Formation_Array_Data(sc,dc,Signals_Numbers)												#получение данных по ID ПРВП и временных слоев из DAT файла

		MaxFrequency=Calculation_MaxFrequency(Frequency)													#вычисление максимальной частоты(приведение ее к большей степени двойки)
		Discretization=MaxFrequency*16*math.ceil(Input_Data[-1,-1])											#вычисление числа точек дискретизации 
		Interpolated_Data=Interpolate_Data(Input_Data,Discretization)										#вычисление интерполяции данных  по числу точек дискретизации
		Spectrum_Amplitude=Amplitude_Spectrum(Interpolated_Data[0:-1])										#получение спектра аплитуд для интерполированных сигналов
		print 'dddd'
		Spectrum_Frequency=Frequency_Spectrum(Interpolated_Data[0:-1])
		Length_Signals_List=len(Output_Signals_List)
		Output_List=list(list() for k in range(Length_Signals_List*3+1))									#формирование выходного списка для записи в файл *.hst
		h=0
		while h<MaxFrequency*Input_Data[-1,-1]:																#выборка необходимого интервала из спектра амплитуд
			if Spectrum_Amplitude[-1,h]>eps:
				for k in range(len(Output_Signals_List)):
					Output_List[k]+=[Spectrum_Amplitude[k,h]/Spectrum_Amplitude[-1,h]]						#вычисление отношения входной амплитуды к выходной
					Output_List[k+Length_Signals_List]+=[Spectrum_Frequency[k,h]-Spectrum_Frequency[-1,h]]
					Output_List[k+Length_Signals_List*2]+=[math.degrees(Spectrum_Frequency[k,h]-Spectrum_Frequency[-1,h])]
				Output_List[-1]+=[h/Input_Data[-1,-1]]														#генерация оси частот
			h+=1

		Named_List=["PhaseResponce_in_Radians.","PhaseResponce_in_Degrees."] 
		Len_Signals_List=len(Output_Signals_List)															#нахождение длины списка сигналов
		for k in Named_List:																				#цикл по приставкам к имени сигнала
			h=0
			while h <Len_Signals_List:																		#цикл по списку сигналов
				Output_Signals_List+=[k+Output_Signals_List[h]]															#добавление ко всем именам сигналов приставки
				h+=1	
		h=0
		while h <Len_Signals_List:																			#добавление приставки
			Output_Signals_List[h]="FrequencyResponce."+Output_Signals_List[h]
			h+=1
		Output_Signals_List=["Frequency"]+Output_Signals_List
		writeFile (Output_List,Output_Signals_List,desc)													#вызов функции записи результатов в файл
		
		misc.SetSolver ("")																					#вывод данных обработки в постпроцессор
		misc.SetPost(os.getenv("DINSYS")+"\dinama\post\Postprocessor")										#вывод данных обработки в постпроцессор
		misc.SetPostFile(desc+".hst")																		#вывод данных обработки в постпроцессор