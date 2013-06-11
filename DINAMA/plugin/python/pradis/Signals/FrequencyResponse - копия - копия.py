# -*- coding: cp1251 -*-
import pradis.engine.functions as f
from include import *
from ParameterValues import *
from scipy.fftpack import *
from string import *
from include import *
from scipy import interpolate
import signal
import scipy
import math
import string
import numpy
import time
import multi
import af
import glb
import misc
import os

class FrequencyResponse:

	def __init__ (self, nl, pl, desc=misc.default):
		 
#------------------------------------getting variables--------------------------------------		
		Scheme=pl[0]
		Dat=pl[1]
		InputSignal=pl[2]
		SpectrumList=pl[3]
		MaxFrequency=pl[4]
		eps=1e-6
#------------------------------------function declarations-----------------------------------		
		def writeFile (dat,name):												# функция записи результатов в файл
			Filehandle = open (desc+".hst", 'w')
			Filehandle.write(desc+"\n\n")
			for i in range(len(name)):
				Filehandle.write (string.ljust(str(name[i]), 41))
			Filehandle.write ("\n")
			for count in range(len(dat[0])):
				i=-1
				while i< (len(dat)-1):
					Filehandle.write (string.rjust(str(dat[i][count]), 41))
					i+=1
				Filehandle.write ("\n")
			Filehandle.close ()	
#------------------------------------main function-----------------------------------
		Position =Scheme.rfind('.')
		Extension=Scheme[Position:]
		Name=Scheme[:Position]
		if Extension=='.sch':
			print "aaaaaa"
			raw_input("Press ENTER to exit")
			os.spawnve(os.P_WAIT, os.getenv("QUCSDIR")+"\bin\qucs", [os.getenv("QUCSDIR")+"\bin\qucs", Scheme], os.environ)
			Dat=Name+'.sch.psl.DAT'

		elif Extension=='.py':
			os.spawnve(os.P_WAIT, os.getenv("DINSYS")+"\Python24\python", [os.getenv("DINSYS")+"\Python24\python", Scheme], os.environ) 
			Dat=Name+'.psl.DAT'
		elif Extension=='.psl':
			os.spawnve(os.P_WAIT, os.getenv("DINSYS")+"\dinama\pradis32\slang", [os.getenv("DINSYS")+"\dinama\pradis32\slang", Scheme], os.environ) 
			Dat=Name+'.psl.DAT'

		sc = af.SolverContext (Dat)												# инициализация контекста решателя
		dc = af.OutVariableContext (sc)											# инициализация контекста ПРВП
		
		SpectrumList+=[InputSignal]
		SpectrumNum=SpectrumList[:]
		for h in range(len(SpectrumList)):										# получение списка ID ПРВП
			for k in range(sc.GetPRVPSize()):
				dc.SetPRVPNumber(k+1)
				if rstrip(dc.GetOVPName())==SpectrumList[h]:
					SpectrumNum[h]=k
		A=scipy.zeros((len(SpectrumList)+1,sc.GetLayerSize()), float)

		for i in range (sc.GetLayerSize()):          							# цикл  по временным слоям. Получение числа временных слоев. Формирование массивов данных.
			dc.SetLayer (i)														# установка текущего временного слоя
			sc.SetLayer(i)														# установка текущего временного слоя. Тоже надо.
			A[-1,i]=sc.GetTime()												# получение текущего времени
			for k in range(len(SpectrumList)):									# цикл получения значений всех интересующих нас переменных на данном временном слое
				A[k,i]=dc.GetOutVariable(SpectrumNum[k])										# получение значения переменной var (номер от 0) на текущем слое	print A
		temp=1
		while MaxFrequency > temp:												#вычисление максимальной частоты
			temp*=2
		MaxFrequency=temp
	
		Tnew=scipy.arange(A[-1,0]+1e-25,A[-1,-1],A[-1,-1]/MaxFrequency)			#разбиение отрезва времени на равные интервалы
		Anew=scipy.zeros((len(SpectrumList)+1,MaxFrequency), float)			
		for h in range(len(SpectrumList)):										#линейная интерполяция данных и получение данных на равных промежутках времени
			f = interpolate.interp1d(A[-1], A[h])
			Anew[h]=f(Tnew)

		for h in range(len(SpectrumList)):										
			Anew[h]=abs(rfft(Anew[h]))*2/MaxFrequency							#преобразование Фурье
		Anew[-1]=scipy.fftpack.helper.rfftfreq(MaxFrequency,1.0/MaxFrequency)
		AFC= list(list() for k in range(len(SpectrumList)))

		for h in range(len(Anew[-1])):
			if Anew[-2,h]>eps:
				for k in range(len(SpectrumList)-1):
					AFC[k]+=[Anew[k,h]/Anew[-2,h]]
				AFC[-1]+=[Anew[-1,h]]
		for h in range(len(SpectrumList)):
			SpectrumList[h]=SpectrumList[h]+"_FrequencyResponse"
		SpectrumList=["Frequency"]+SpectrumList
		
		writeFile (AFC,SpectrumList)											# вызов функции записи результатов в файл

		misc.SetSolver ("")														#вывод данных обработки в постпроцессор
		misc.SetPost(os.getenv("DINSYS")+"\dinama\post\Postprocessor")			#вывод данных обработки в постпроцессор
		misc.SetPostFile(desc+".hst")											#вывод данных обработки в постпроцессор