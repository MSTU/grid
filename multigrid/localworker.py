import pickle
from solvers.holder import get_solver

def run_task(task):
	for lc in task.loadcases:
		solver = get_solver(lc.solver)
		solver.preexecute(lc)
		task.result[lc.name] = solver.run(lc, pickle.loads(task.input_params))
	task.recalc_status()
	return task
