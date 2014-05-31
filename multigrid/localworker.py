import os
import pickle

import constants
from solvers.holder import get_solver


def run_task(task):
	# save current directory
	cwd = os.getcwd()
	# move to 'loadcases' directory
	directory = os.path.join(cwd, constants.LOADCASES_DIR)
	if not os.path.exists(directory):
		os.makedirs(directory)
	os.chdir(directory)

	try:
		for lc in task.loadcases:
			solver = get_solver(lc.solver)
			lc.task_id = task.id
			try:
				task.result[lc.name] = solver.run(lc, pickle.loads(task.input_params))
			except Exception as e:
				if task.is_exceptions_used:
					raise e
				else:
					lc.status = constants.ERROR_STATUS
					task.result[lc.name] = {'error': True, 'exception': e}
			# if exceptions doesn't occur and status not set to error set it to success
			if not lc.status is constants.ERROR_STATUS:
				lc.status = constants.SUCCESS_STATUS

		task.recalc_status()

		return task

	finally:
		# move to parent directory
		os.chdir(cwd)
