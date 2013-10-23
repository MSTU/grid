from conf import ConfigHost


def RunTask(task):
	config = ConfigHost.ConfigHost()
	for i in task.lc:
		solver = config.solvers[i.Solver]
		solver.Init()
		status = solver.Run(i, task.ma)
		if status < task.GetModelAnalysis().GetStatus():
			task.ma.SetStatus(status)

	print "Parameters = " + str(task.ma.GetParameters())
	print "Results = " + str(task.ma.GetResults())
	return task
