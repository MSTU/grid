# -*- coding: cp1251 -*-

# ***************************************************************************
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

import json

from conf import configclient
from task import Task


try:
	from celery.result import AsyncResult
except:
	pass

from localworker import run_task as local_run

try:
	from remoteworker import run_task as remote_run
except:
	pass


def run_fileserver():
	pass


class MultiGrid:
	def __init__(self, is_local_work=False):
		"""
		is_local_work : bool
			True if system will using on local machine without celery, False otherwise
		"""
		self._is_local_work = is_local_work
		if self._is_local_work:
			self._id_to_task = dict()
			self._task_counter = 0

	def calculate(self, loadcases, input_list):
		"""
		For all items in input_list create Task instance and run them.
		Return ids of created Tasks
		"""
		if not isinstance(loadcases, list):
			loadcases = [loadcases]
		# if some loadcases needed in filetransfer, run ftp server
		# for loadcase in loadcases:
		# 	if loadcase.need_filetransfer:
		# 		run_fileserver()
		# 		break
		result_ids = []
		if isinstance(input_list, dict):
			input_list = _dict_to_list(input_list)
		for item in input_list:
			task = Task(loadcases, item)
			if not self._is_local_work:
				async_result = remote_run.delay(task)
				task.id = async_result.task_id
				result_ids.append(task.id)
			else:
				self._task_counter += 1
				result_ids.append(self._task_counter)
				#TODO error handling
				self._id_to_task[self._task_counter] = local_run(task)
		return result_ids

	def get(self, result_ids):
		"""
		Wait and return result of tasks with ids specified in result_ids list
		"""
		results = []
		for result_id in result_ids:
			try:
				if not self._is_local_work:
					async_result = AsyncResult(result_id)
					result_task = async_result.get()
				else:
					result_task = self._id_to_task.pop(result_id)
				# it's new instance of Task, therefore need to reassign id field
				result_task.id = result_id
			except Exception as e:
				#TODO right error handling
				result_task = None
			results.append(result_task.result)
		result_dict = _list_to_dict(results)
		# if only one loadcase calculated, return value of the one loadcase
		# else return all dictionary
		#if len(result_dict) is 1:
		#	return result_dict[result_dict.keys()[0]]
		#else:
		return result_dict

	def map(self, loadcases, input_list):
		"""
		Run all tasks, wait results and return them
		"""
		result_ids = self.calculate(loadcases, input_list)
		return self.get(result_ids)

	def ready(self, result_ids):
		"""
		Check if task is ready
		"""
		if not self._is_local_work:
			if isinstance(result_ids, list):
				for result_id in result_ids:
					if not AsyncResult(result_id).ready():
						return False
			else:
				return AsyncResult(result_ids).ready()

		return True

	def reload(self):
		"""
		Reinit instance
		"""
		self.__init__(self._is_local_work)

	def web_get(self, result_ids):
		import urllib2

		if not isinstance(result_ids, list):
			result_ids = [result_ids]

		results = []
		for result_id in result_ids:
			try:
				response = urllib2.urlopen(
					'http://' + configclient.WEB_SERVER_ADDRESS + ':' + configclient.WEB_SERVER_PORT +
					'/api/get_result/' + str(result_id) + '/').read()
				result = json.loads(response)
			except Exception:
				result = None
		results.append(result)
		# result_dict = _list_to_dict(results)
		# return result_dict
		if len(results) == 1:
			return results[0]
		return results

	def web_get_ids(self, job_name):
		import urllib2

		try:
			response = urllib2.urlopen(
				'http://' + configclient.WEB_SERVER_ADDRESS + ':' + configclient.WEB_SERVER_PORT +
				'/api/get_ids/' + job_name + '/').read()
			result = json.loads(response)
		except Exception:
			result = None
		return result

	def web_get_results_from_job(self, job_name):
		import urllib2

		try:
			response = urllib2.urlopen(
				'http://' + configclient.WEB_SERVER_ADDRESS + ':' + configclient.WEB_SERVER_PORT +
				'/api/get_results_from_job/' + job_name + '/').read()
			result = json.loads(response)
		except Exception:
			result = None
		return result


def _list_to_dict(list_):
	"""
	Convert list of dictionaries with equals keys to dictionary of lists
	[{'a':1,'b':2}, {'a':3, 'b':4}] -> {'a':[1,3], 'b':[2,4]}
	"""
	result = dict()
	# init dict by lists
	for key, value in list_[0].iteritems():
		result[key] = []
	for item in list_:
		for key, value in item.iteritems():
			result[key].append(value)
	return result


def _dict_to_list(dict_):
	"""
	Convert dictionary of lists to list of dictionaries with equals keys
	{'a':[1,3], 'b':[2,4]} -> [{'a':1,'b':2}, {'a':3, 'b':4}]
	"""
	result = []
	is_lists_equal = True
	list_len = 0
	keys = dict_.keys()
	# check if list in dictionary is equal
	for key, value in dict_.iteritems():
		if list_len:
			is_lists_equal &= (list_len == len(value))
		else:
			list_len = len(value)

	if is_lists_equal:
		for i in xrange(list_len):
			item = dict()
			for key in keys:
				item[key] = dict_[key][i]
			result.append(item)
		return result
	else:
		# TODO handle this case
		return []
