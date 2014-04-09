# -*- coding: cp1251 -*-

#***************************************************************************
#
#    copyright            : (C) 2013 by Valery Ovchinnikov (LADUGA Ltd.)
#                                       Anton Lapshin
#                                       Anton Kargin
#    email                : laduga@laduga.com
#***************************************************************************
#***************************************************************************
#*                                                                         *
#*   This program is free software; you can redistribute it and/or modify  *
#*   it under the terms of the GNU General Public License as published by  *
#*   the Free Software Foundation; either version 2 of the License, or     *
#*   (at your option) any later version.                                   *
#*                                                                         *
#***************************************************************************/
from pradis.multi.Variable import Variable
from multigrid.solvers.modelica import ModelicaLoadcase
from GA_Modelica import GA
from numpy import exp
from scipy import integrate, interpolate
import solvers.modelica_api as api
from multigrid import map as multimap
import matplotlib.pyplot as plt
import time

def objective_function(results):
	#last_layer = api.layer_count(results)-1
	'''
	for key in results:
		last_layer = len(results[key])-1
		break
	'''
	#t = api.value_from_layer(results, 'time', last_layer)
	return integrate.quad(integrand, 0, 4.0, args=results, epsabs=1.49e-05, epsrel=1.49e-05, limit=200)[0],

def integrand(t, results_dict):
	y_ref = 0.5 * (1.0 - exp(-5.0*t))
	y = api.value(results_dict, 'mass1.s', t)
	return (y_ref - y)**2

def get_value_from_layer_by_name(result_dict, key, index):
	"""
	Returns value from dictionary "dict" for key named "key" from time layer with number "index"
	index - it is index in the list of values
	dictionary has following structure:
	{'key1': [value1, value2, value3, ...], 'key2': [value1, value2, value3, ...], ...}

	"""
	if key in result_dict:
		return result_dict[key][index]
	else:
		print 'ERROR: there is no key "' + key + '" in dictionary'
		return None

def f(results_dict, var_name):
	"""
	Returns list of values for specified variable name "var_name"
	"""
	if var_name in results_dict:
		return results_dict[var_name]
	else:
		print 'ERROR: there is no key "' + var_name + '" in dictionary'
		return None

def get_value(results_dict, var_name, time):
	t = f(results_dict, 'time')
	v = f(results_dict, var_name)
	func = interpolate.interp1d(t, v)
	return func(time)

def y_ref(t):
	l = []
	for item in t:
		l.append(0.5 * (1.0 - exp(-5.0*item)))
	return l

def test():
	la = ModelicaLoadcase('mos/linear_actuator.mo', desc='linear_actuator',
						  solver_params={'startTime': 0.0, 'stopTime': 4.0, 'stepSize': 0.01})
	var1 = Variable([], ['springdamper1.d', 2.0, 1, 40], desc='sd1')
	var2 = Variable([], ['springdamper2.d', 3.0, 1, 40], desc='sd2')
	ga = GA('', [la, [var1, var2], objective_function, 0.5, 0.2, 0.05, 100, 10])
	start_time = time.time()
	ga.run()
	print 'execution time:', time.time() - start_time, "seconds"
	'''
	par_dict = {}
	par_dict['springdamper1.d'] = 20.26010902#19.88
	par_dict['springdamper2.d'] = 4.06789479#4.90
	input_list = []
	input_list.append(par_dict)
	results = multimap(la, input_list)[la.name][0]
	print objective_function(results)
	t = api.value_list(results, 'time')
	v = api.value_list(results, 'mass1.s')
	func = interpolate.interp1d(t, v)
	plt.plot(t, func(t))
	plt.plot(t, y_ref(t))
	plt.text(0.5, 0.3, 'd1=20.26010902')
	plt.text(0.5, 0.2, 'd2=4.06789479')
	plt.text(0.5, 0.1, 'fitness=0.006849501332322377')
	plt.show()
	'''

test()