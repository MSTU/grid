from conf import confighost

def run_task(task):
	config = confighost.ConfigHost()
	for lc in task.loadcases:
		solver = config.solvers[lc.solver]
		solver.init()
		task.result_params[lc.name] = solver.run(lc, task.input_params)
	task.recalc_status()

	return task
