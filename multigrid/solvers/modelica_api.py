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
from scipy import interpolate

def value(result_dict, var_name, time, kind='linear'):
	"""
	:param result_dict: dictionary of results, where
	key - name of variable in Modelica model
	value - list of values at each time layer
	:param var_name: name of variable in Modelica model
	:param time: value of time, at which you want to get the value of variable called "var_name"
	:param kind: specifies the kind of interpolation as a string
	(�linear�, �nearest�, �zero�, �slinear�, �quadratic, �cubic�, where �slinear�, �quadratic� and �cubic�
	refer to a spline interpolation of first, second or third order) or as an integer specifying the order
	of the spline interpolator to use. Default is �linear�.
	:return: value of variable called "var_name" at time "time" (var_name(time))
	"""
	# t = value_list(result_dict, 'time')
	# v = value_list(result_dict, var_name)
	# f = interpolate.interp1d(t, v, kind)
	# return f(time)
	if var_name in result_dict.keys():
		t = value_list(result_dict, 'time')
		v = value_list(result_dict, var_name)
		f = interpolate.interp1d(t, v, kind)
		return f(time)
	else:
		lc_name = var_name.split('.')[0]
		var_name = var_name.replace(lc_name+'.', '')
		t = value_list(result_dict[lc_name], 'time')
		v = value_list(result_dict[lc_name], var_name)
		f = interpolate.interp1d(t, v, kind)
		return f(time)


def value_from_layer(result_dict, var_name, layer_index):
	"""
	:param result_dict: dictionary of results, where
	key - name of variable in Modelica model
	value - list of values at each time layer
	:param var_name: name of variable in Modelica model
	:param layer_index: index of time layer at which you need a value
	:return: value of variable called "var_name" at time layer with index "layer_index"
	"""
	if var_name in result_dict:
		return result_dict[var_name][layer_index]
	else:
		print 'ERROR: there is no key "' + var_name + '" in result dictionary'
		return None

def value_list(result_dict, var_name):
	"""
	:param result_dict: dictionary of results, where
	key - name of variable in Modelica model
	value - list of values at each time layer
	:param var_name: name of variable in Modelica model
	:return: list of values for variable called "var_name"
	"""
	if var_name in result_dict:
		return result_dict[var_name]
	else:
		print 'ERROR: there is no key "' + var_name + '" in result dictionary'
		return None

def layer_count(result_dict):
	"""
	:param result_dict: dictionary of results, where
	key - name of variable in Modelica model
	value - list of values at each time layer
	:return: number of time layers
	"""
	return len(result_dict.values()[0])

def convert_keys(results):
	"""
	Converts loadcase keys in dictionary of results.
	After this conversion you can use PRADIS loadcase names to access results
	Parameters:
	1) results - dictionary of results
	keys - loadcases' names
	values - list of values for Python loadcases and list of dictionaries for Modelica loadcases.
	Returns:
	dictionary with modified keys and the same values
	"""
	temp_keys = results.keys()
	keys = []
	d = {}
	for key in temp_keys:
		key = key.split('.')[-1]
		keys.append(key)
	values = results.values()
	for key, value in zip(keys, values):
		d[key] = value
	return d

def criterion_dictionary(index, results):
	"""
	Creates input dictionary for use in criterions.
	keys - loadcases' names
	values - scalar value for Python loadcase and dictionary for Modelica loadcase
	(key - name of output variable, value - value of output variable)
	Parameters:
	1) index - index of required data in list of results for each loadcase.
	Format of "results" dictionary:
	{'loadcase_1_name': [{}, {}, ...], 'loadcase_2_name': [{}, {}, ...], ...}
	results[loadcase_name][index] = {}
	2) results - dictionary of results that was returned by MultiGRID function "map"
	Returns:
	dictionary to use in criterions
	"""
	d = {}
	for loadcase in results:
		d[loadcase] = results[loadcase][index]
	return d
