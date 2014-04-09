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
	for lc in task.loadcases:
		solver = get_solver(lc.solver)
		task.result[lc.name] = solver.run(lc, pickle.loads(task.input_params))
	#task.recalc_status()
	# move to parent directory
	os.chdir(cwd)
	return task
