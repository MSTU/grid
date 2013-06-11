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