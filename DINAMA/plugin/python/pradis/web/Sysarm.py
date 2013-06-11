# -*- coding: cp1251 -*-

import random
import os

from pradis.web.Model import *
from pradis.web.Parameter import *

systemDir = os.getenv('dinsys')+'/DINAMA/'
webDir = systemDir + "sysarm/web/"


class Sysarm:

	def __init__(self):

		self.init ()

	def getModelList(self):
	
		return self.modelList
	

		
	def init(self):
	
		self.modelList = []
		for i in range (5):
			model = Model("model_"+str(i))
			np = random.randint (0,5)
			
			for j in range (np):
				par = Parameter ("par_"+str(j), "", j, "Параметр "+str(i))
				model.add_par(par)
			
			self.modelList.append (model)
	
	