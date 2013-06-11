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
		sc = af.SolverContext (Dat)																			#инициализация контекста решателя
		dc = af.OutVariableContext (sc)																		#инициализация контекста ПРВП
			
		Output_Signals_Numbers=Getting_List_ID(Output_Signals_List,sc,dc)									#получение списка ID ПРВП
		Input_Data=Formation_Array_Data(sc,dc,Output_Signals_Numbers)										#получение данных по ID ПРВП и временных слоев из DAT файла
		MaxFrequency=Calculation_MaxFrequency(Frequency)													#вычисление максимальной частоты(приведение ее к большей степени двойки)
		Discretization=MaxFrequency*16*math.ceil(Input_Data[-1,-1])											#вычисление числа точек дискретизации 
		Interpolated_Data=Interpolate_Data(Input_Data,Discretization)										#вычисление интерполяции данных  по числу точек дискретизации
		Spectrum=Amplitude_Spectrum(Interpolated_Data[0:-1])												#получение спектра аплитуд для интерполированных сигналов
		print 'sssss'
		Output_List=scipy.zeros((len(Spectrum)*2+1,MaxFrequency*math.ceil(Input_Data[-1,-1])), float)		#формирование выходного списка для записи в файл *.hst

		for k in range(len(Spectrum)):
			Output_List[k]=Spectrum[k,:MaxFrequency*math.ceil(Input_Data[-1,-1])]							#выборка необходимого интервала из спектра амплитуд
			Output_List[k+len(Spectrum)]=Spectrum[k,:MaxFrequency*math.ceil(Input_Data[-1,-1])]**2			#получение квадратов амплитуд(плотность спектра)
		h=0
		while h<MaxFrequency*math.ceil(Input_Data[-1,-1]):													
			Output_List[-1,h]=h/Input_Data[-1,-1]															#генерация оси частот
			h+=1

		for h in range(len(Output_Signals_List)):															#создание списка имен выходных параметров
			Output_Signals_List+=["PSD."+Output_Signals_List[h]]
			Output_Signals_List[h]="Spectrum."+Output_Signals_List[h]
		Output_Signals_List=["Frequency"]+Output_Signals_List
	
		writeFile (Output_List,Output_Signals_List,desc)													#вызов функции записи результатов в файл
		
		misc.SetSolver ("")																					#вывод данных обработки в постпроцессор
		misc.SetPost(os.getenv("DINSYS")+"\dinama\post\Postprocessor")										#вывод данных обработки в постпроцессор
		misc.SetPostFile(desc+".hst")																		#вывод данных обработки в постпроцессор