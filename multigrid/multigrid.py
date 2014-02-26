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
from task import Task
from celery.result import AsyncResult

from localworker import run_task as local_run
from remoteworker import run_task as remote_run

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
		result_ids = []
		if isinstance(input_list, dict):
			input_list = MultiGrid._dict_to_list(input_list)
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
			except Exception as e:
				#TODO right error handling
				result_task = None
			results.append(result_task.result)
		result_dict = MultiGrid._list_to_dict(results)
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
		is_ready = True
		if not self._is_local_work:
			if isinstance(result_ids, list):
				for result_id in result_ids:
					is_ready &= AsyncResult(result_id).ready()
					if not is_ready:
						break
			else:
				is_ready &= AsyncResult(result_ids).ready()

		return is_ready

	def reload(self):
		"""
		Reinit instance
		"""
		self.__init__(self._is_local_work)

	@staticmethod
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

	@staticmethod
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
