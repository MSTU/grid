import os
import pickle
import constants
from solvers.holder import get_solver


def run_task(task):
	for lc in task.loadcases:
		solver = get_solver(lc.solver)
		lc.task_id = task.id
		task.result[lc.name] = solver.run(lc, pickle.loads(task.input_params))
	task.recalc_status()

	return task
