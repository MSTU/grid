from conf import ConfigHost


def RunTask(task):
	config = ConfigHost.ConfigHost()
	for lc in task.loadcases:
		solver = config.solvers[lc.solver]
		solver.Init()
		task.result_params[lc.name] = solver.Run(lc, task.input_params)
	task.recalcStatus()

	print "Parameters = " + str(task.input_params)
	print "Results = " + str(task.result_params)
	return task
