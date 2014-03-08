import unittest

from multigrid.multigrid import MultiGrid
from solvers.modelicasolver import ModelicaLoadcase
from solvers.pythonsolver import PythonLoadcase

def f(x):
	return x * x


def f1(xy):
	return xy[0] / xy[1]

class LocalTest(unittest.TestCase):
	def setUp(self):
		self.mg = MultiGrid(True)

	def test_1(self):
		lc = PythonLoadcase(f)
		input_list = range(1, 10)
		result_list = self.mg.map(lc, input_list)[f.__name__]
		self.assertEqual(result_list, map(f, input_list))

	def test_2(self):
		lc_name = 'lc'
		lc = ModelicaLoadcase('mos/mydcmotor.mo', lc_name, solver_params={'startTime': 0.0, 'stopTime': 10.0, 'numberOfIntervals': 10})

		input = dict()
		input['resistor1.R'] = [5.0, 2.0]
		input['inductor1.L'] = [0.4, 1.0]
		input['load.J'] = [2.0, 0.5]

		result = self.mg.map(lc, input)
		right_result = [{'der(load.w)': [0.0, -0.0830801363154827, -0.06790978474217732, -0.0555094881755961, -0.04537341103779208, -0.03708819415498805], 'load.a': [0.0, -0.0830801363154827, -0.06790978474217732, -0.0555094881755961, -0.04537341103779208, -0.03708819415498805], 'emf1.flange.phi': [0.0, -0.1745466209958222, -0.6818810327924953, -1.461772546716575, -2.464448505062024, -3.649237060061404], 'signalVoltage1.n.i': [-0.0, 0.1661602726309654, 0.1358195694843546, 0.1110189763511922, 0.09074682207558417, 0.0741763883099761], 'ground1.p.v': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 'load.w': [0.0, -0.1758989269951751, -0.3263791139413721, -0.4493819862742905, -0.5499252766107704, -0.632109238461457], 'signalVoltage1.i': [0.0, -0.1661602726309654, -0.1358195694843546, -0.1110189763511922, -0.09074682207558417, -0.0741763883099761], 'emf1.internalSupport.tau': [0.0, -0.1661602726309654, -0.1358195694843546, -0.1110189763511922, -0.09074682207558417, -0.0741763883099761], 'emf1.fixed.flange.phi': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 'signalVoltage1.v': [1.0, 1.0, 1.0, 1.0, 1.0, 1.0], 'resistor1.LossPower': [0.0, 0.1380461810039837, 0.0922347772745772, 0.06162606555033286, 0.04117492858408865, 0.02751068291356179], 'ground1.p.i': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 'signalVoltage1.n.v': [-1.0, -1.0, -1.0, -1.0, -1.0, -1.0], 'inductor1.p.i': [0.0, -0.1661602726309654, -0.1358195694843546, -0.1110189763511922, -0.09074682207558417, -0.0741763883099761], 'resistor1.T_heatPort': [300.15, 300.15, 300.15, 300.15, 300.15, 300.15], 'load.phi': [0.0, -0.1745466209958222, -0.6818810327924953, -1.461772546716575, -2.464448505062024, -3.649237060061404], 'inductor1.p.v': [-1.0, -0.169198636845173, -0.3209021525782267, -0.444905118244039, -0.5462658896220791, -0.6291180584501195], 'load.flange_a.phi': [0.0, -0.1745466209958222, -0.6818810327924953, -1.461772546716575, -2.464448505062024, -3.649237060061404], 'emf1.w': [0.0, -0.1758989269951751, -0.3263791139413721, -0.4493819862742905, -0.5499252766107704, -0.632109238461457], 'emf1.v': [0.0, -0.1758989269951751, -0.3263791139413721, -0.4493819862742905, -0.5499252766107704, -0.632109238461457], 'emf1.internalSupport.phi': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 'signalVoltage1.p.v': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 'inductor1.n.v': [0.0, -0.1758989269951751, -0.3263791139413721, -0.4493819862742905, -0.5499252766107704, -0.632109238461457], 'inductor1.i': [0.0, -0.1661602726309654, -0.1358195694843546, -0.1110189763511922, -0.09074682207558417, -0.0741763883099761], 'inductor1.v': [-1.0, 0.006700290150002064, 0.005476961363145405, 0.004476868030251546, 0.003659386988691282, 0.002991180011337469], 'inductor1.n.i': [-0.0, 0.1661602726309654, 0.1358195694843546, 0.1110189763511922, 0.09074682207558417, 0.0741763883099761], 'emf1.phi': [0.0, -0.1745466209958222, -0.6818810327924953, -1.461772546716575, -2.464448505062024, -3.649237060061404], 'emf1.i': [0.0, -0.1661602726309654, -0.1358195694843546, -0.1110189763511922, -0.09074682207558417, -0.0741763883099761], 'emf1.internalSupport.flange.phi': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 'load.flange_a.tau': [0.0, -0.1661602726309654, -0.1358195694843546, -0.1110189763511922, -0.09074682207558417, -0.0741763883099761], 'resistor1.n.v': [-1.0, -0.169198636845173, -0.3209021525782267, -0.444905118244039, -0.5462658896220791, -0.6291180584501195], 'resistor1.p.i': [0.0, -0.1661602726309654, -0.1358195694843546, -0.1110189763511922, -0.09074682207558417, -0.0741763883099761], 'emf1.fixed.flange.tau': [-0.0, 0.1661602726309654, 0.1358195694843546, 0.1110189763511922, 0.09074682207558417, 0.0741763883099761], 'load.flange_b.phi': [0.0, -0.1745466209958222, -0.6818810327924953, -1.461772546716575, -2.464448505062024, -3.649237060061404], 'resistor1.i': [0.0, -0.1661602726309654, -0.1358195694843546, -0.1110189763511922, -0.09074682207558417, -0.0741763883099761], 'emf1.flange.tau': [-0.0, 0.1661602726309654, 0.1358195694843546, 0.1110189763511922, 0.09074682207558417, 0.0741763883099761], 'resistor1.p.v': [-1.0, -1.0, -1.0, -1.0, -1.0, -1.0], 'step1.y': [1.0, 1.0, 1.0, 1.0, 1.0, 1.0], 'resistor1.n.i': [-0.0, 0.1661602726309654, 0.1358195694843546, 0.1110189763511922, 0.09074682207558417, 0.0741763883099761], 'der(inductor1.i)': [-2.5, 0.01675072537500516, 0.01369240340786351, 0.01119217007562887, 0.009148467471728206, 0.007477950028343672], 'load.flange_b.tau': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 'resistor1.R_actual': [5.0, 5.0, 5.0, 5.0, 5.0, 5.0], 'resistor1.v': [0.0, -0.830801363154827, -0.6790978474217733, -0.555094881755961, -0.4537341103779208, -0.3708819415498805], 'der(load.phi)': [0.0, -0.1758989269951751, -0.3263791139413721, -0.4493819862742905, -0.5499252766107704, -0.632109238461457], 'emf1.n.i': [-0.0, 0.1661602726309654, 0.1358195694843546, 0.1110189763511922, 0.09074682207558417, 0.0741763883099761], 'emf1.p.v': [0.0, -0.1758989269951751, -0.3263791139413721, -0.4493819862742905, -0.5499252766107704, -0.632109238461457], 'emf1.p.i': [0.0, -0.1661602726309654, -0.1358195694843546, -0.1110189763511922, -0.09074682207558417, -0.0741763883099761], 'emf1.n.v': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 'signalVoltage1.p.i': [0.0, -0.1661602726309654, -0.1358195694843546, -0.1110189763511922, -0.09074682207558417, -0.0741763883099761], 'emf1.internalSupport.flange.tau': [0.0, -0.1661602726309654, -0.1358195694843546, -0.1110189763511922, -0.09074682207558417, -0.0741763883099761], 'time': [0.0, 2.0, 4.0, 6.0, 8.0, 10.0], 'der(emf1.phi)': [0.0, -0.1758989269951751, -0.3263791139413721, -0.4493819862742905, -0.5499252766107704, -0.632109238461457]}, {'der(load.w)': [0.0, -0.2461201764474222, 0.02772621959678204, 0.001384054599547402, -0.0006643351916665881, 4.998129994894026e-05], 'load.a': [0.0, -0.2461201764474222, 0.02772621959678204, 0.001384054599547402, -0.0006643351916665881, 4.998129994894026e-05], 'emf1.flange.phi': [0.0, -0.9436797560323213, -2.988029246578736, -5.002380392462413, -6.999950331149864, -8.999961926682971], 'signalVoltage1.n.i': [-0.0, 0.1230600882237111, -0.01386310979839102, -0.0006920272997737011, 0.0003321675958332941, -2.499064997447013e-05], 'ground1.p.v': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 'load.w': [0.0, -0.9332601557441395, -1.025833863219526, -0.9983116348371833, -0.9997175012480537, -1.00006306396111], 'signalVoltage1.i': [0.0, -0.1230600882237111, 0.01386310979839102, 0.0006920272997737011, -0.0003321675958332941, 2.499064997447013e-05], 'emf1.internalSupport.tau': [0.0, -0.1230600882237111, 0.01386310979839102, 0.0006920272997737011, -0.0003321675958332941, 2.499064997447013e-05], 'emf1.fixed.flange.phi': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 'signalVoltage1.v': [1.0, 1.0, 1.0, 1.0, 1.0, 1.0], 'resistor1.LossPower': [0.0, 0.03028757062725512, 0.0003843716265644902, 9.5780356726416e-07, 2.206706234433412e-07, 1.249065172292968e-09], 'ground1.p.i': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 'signalVoltage1.n.v': [-1.0, -1.0, -1.0, -1.0, -1.0, -1.0], 'inductor1.p.i': [0.0, -0.1230600882237111, 0.01386310979839102, 0.0006920272997737011, -0.0003321675958332941, 2.499064997447013e-05], 'resistor1.T_heatPort': [300.15, 300.15, 300.15, 300.15, 300.15, 300.15], 'load.phi': [0.0, -0.9436797560323213, -2.988029246578736, -5.002380392462413, -6.999950331149864, -8.999961926682971], 'inductor1.p.v': [-1.0, -0.7538798235525778, -1.027726219596782, -1.001384054599547, -0.9993356648083334, -1.000049981299949], 'load.flange_a.phi': [0.0, -0.9436797560323213, -2.988029246578736, -5.002380392462413, -6.999950331149864, -8.999961926682971], 'emf1.w': [0.0, -0.9332601557441395, -1.025833863219526, -0.9983116348371833, -0.9997175012480537, -1.00006306396111], 'emf1.v': [0.0, -0.9332601557441395, -1.025833863219526, -0.9983116348371833, -0.9997175012480537, -1.00006306396111], 'emf1.internalSupport.phi': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 'signalVoltage1.p.v': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 'inductor1.n.v': [0.0, -0.9332601557441395, -1.025833863219526, -0.9983116348371833, -0.9997175012480537, -1.00006306396111], 'inductor1.i': [0.0, -0.1230600882237111, 0.01386310979839102, 0.0006920272997737011, -0.0003321675958332941, 2.499064997447013e-05], 'inductor1.v': [-1.0, 0.1793803321915617, -0.001892356377255933, -0.003072419762364054, 0.00038183643972034, 1.308266116128998e-05], 'inductor1.n.i': [-0.0, 0.1230600882237111, -0.01386310979839102, -0.0006920272997737011, 0.0003321675958332941, -2.499064997447013e-05], 'emf1.phi': [0.0, -0.9436797560323213, -2.988029246578736, -5.002380392462413, -6.999950331149864, -8.999961926682971], 'emf1.i': [0.0, -0.1230600882237111, 0.01386310979839102, 0.0006920272997737011, -0.0003321675958332941, 2.499064997447013e-05], 'emf1.internalSupport.flange.phi': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 'load.flange_a.tau': [0.0, -0.1230600882237111, 0.01386310979839102, 0.0006920272997737011, -0.0003321675958332941, 2.499064997447013e-05], 'resistor1.n.v': [-1.0, -0.7538798235525778, -1.027726219596782, -1.001384054599547, -0.9993356648083334, -1.000049981299949], 'resistor1.p.i': [0.0, -0.1230600882237111, 0.01386310979839102, 0.0006920272997737011, -0.0003321675958332941, 2.499064997447013e-05], 'emf1.fixed.flange.tau': [-0.0, 0.1230600882237111, -0.01386310979839102, -0.0006920272997737011, 0.0003321675958332941, -2.499064997447013e-05], 'load.flange_b.phi': [0.0, -0.9436797560323213, -2.988029246578736, -5.002380392462413, -6.999950331149864, -8.999961926682971], 'resistor1.i': [0.0, -0.1230600882237111, 0.01386310979839102, 0.0006920272997737011, -0.0003321675958332941, 2.499064997447013e-05], 'emf1.flange.tau': [-0.0, 0.1230600882237111, -0.01386310979839102, -0.0006920272997737011, 0.0003321675958332941, -2.499064997447013e-05], 'resistor1.p.v': [-1.0, -1.0, -1.0, -1.0, -1.0, -1.0], 'step1.y': [1.0, 1.0, 1.0, 1.0, 1.0, 1.0], 'resistor1.n.i': [-0.0, 0.1230600882237111, -0.01386310979839102, -0.0006920272997737011, 0.0003321675958332941, -2.499064997447013e-05], 'der(inductor1.i)': [-1.0, 0.1793803321915617, -0.001892356377255933, -0.003072419762364054, 0.00038183643972034, 1.308266116128998e-05], 'load.flange_b.tau': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 'resistor1.R_actual': [2.0, 2.0, 2.0, 2.0, 2.0, 2.0], 'resistor1.v': [0.0, -0.2461201764474222, 0.02772621959678204, 0.001384054599547402, -0.0006643351916665881, 4.998129994894026e-05], 'der(load.phi)': [0.0, -0.9332601557441395, -1.025833863219526, -0.9983116348371833, -0.9997175012480537, -1.00006306396111], 'emf1.n.i': [-0.0, 0.1230600882237111, -0.01386310979839102, -0.0006920272997737011, 0.0003321675958332941, -2.499064997447013e-05], 'emf1.p.v': [0.0, -0.9332601557441395, -1.025833863219526, -0.9983116348371833, -0.9997175012480537, -1.00006306396111], 'emf1.p.i': [0.0, -0.1230600882237111, 0.01386310979839102, 0.0006920272997737011, -0.0003321675958332941, 2.499064997447013e-05], 'emf1.n.v': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 'signalVoltage1.p.i': [0.0, -0.1230600882237111, 0.01386310979839102, 0.0006920272997737011, -0.0003321675958332941, 2.499064997447013e-05], 'emf1.internalSupport.flange.tau': [0.0, -0.1230600882237111, 0.01386310979839102, 0.0006920272997737011, -0.0003321675958332941, 2.499064997447013e-05], 'time': [0.0, 2.0, 4.0, 6.0, 8.0, 10.0], 'der(emf1.phi)': [0.0, -0.9332601557441395, -1.025833863219526, -0.9983116348371833, -0.9997175012480537, -1.00006306396111]}]
		self.assertEqual(result[lc_name], right_result)

	def test_3(self):
		lc = PythonLoadcase(f1)
		x_list = range(10, 20)
		y_list = range(10)
		result = self.mg.map(lc, [(x, y) for x, y in zip(x_list, y_list)])[f1.__name__]
		#TODO right error handling and status checking


def test_suite():
	return unittest.TestLoader().loadTestsFromTestCase(LocalTest)


if __name__ == '__main__':
	unittest.main()