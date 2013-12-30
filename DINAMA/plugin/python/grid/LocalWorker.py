from conf import ConfigHost


def RunTask(task):
	config = ConfigHost.ConfigHost()
	for i in task.lc:
		solver = config.solvers[i.solver]
		solver.Init()
		status = solver.Run(i, task)
		if status < task.status:
			task.status = status

	print "Parameters = " + str(task.input_params)
	print "Results = " + str(task.result_params)
	return task
