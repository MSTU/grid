model dcmotor
  //Observe the difference between MSL 2.2 and 3.1 regarding the default values, in 3.1 there are no default values set, only start values
  // Modelica version 3.1
  // Modelica.Mechanics.Rotational.Inertia         load(J = 1); // Modelica version 2.2
  Modelica.Blocks.Sources.Step step1 annotation(Placement(visible = true, transformation(origin = {-79.4773,16.2338}, extent = {{-12,-12},{12,12}}, rotation = 0)));
  Modelica.Electrical.Analog.Basic.Resistor resistor1(R = 10) annotation(Placement(visible = true, transformation(origin = {-15.8154,53.3825}, extent = {{-12,-12},{12,12}}, rotation = 0)));
  Modelica.Electrical.Analog.Basic.EMF emf1 annotation(Placement(visible = true, transformation(origin = {53.2417,22.0776}, extent = {{-12,-12},{12,12}}, rotation = 0)));
  Modelica.Electrical.Analog.Basic.Ground ground1 annotation(Placement(visible = true, transformation(origin = {10.9074,-28.1522}, extent = {{-12,-12},{12,12}}, rotation = 0)));
  Modelica.Electrical.Analog.Basic.Inductor inductor1(L = 0.2) annotation(Placement(visible = true, transformation(origin = {21.1619,53.3711}, extent = {{-12,-12},{12,12}}, rotation = 0)));
  Modelica.Mechanics.Rotational.Components.Inertia load(J = 1) annotation(Placement(visible = true, transformation(origin = {85.7499,21.8942}, extent = {{-12,-12},{12,12}}, rotation = 0)));
  Modelica.Electrical.Analog.Sources.SignalVoltage signalVoltage1 annotation(Placement(visible = true, transformation(origin = {-41.9801,16.1514}, extent = {{12,-12},{-12,12}}, rotation = 90)));
equation
  connect(ground1.p,emf1.n) annotation(Line(points = {{10.9074,-16.1522},{10.9074,-16.5289},{53.1287,-16.5289},{53.1287,10.0776},{53.2417,10.0776}}));
  connect(inductor1.n,emf1.p) annotation(Line(points = {{33.1619,53.3711},{53.3648,53.3711},{53.3648,34.0776},{53.2417,34.0776}}));
  connect(emf1.flange,load.flange_a) annotation(Line(points = {{65.2417,22.0776},{78.1726,22.0776},{78.1726,21.8942},{73.7499,21.8942}}));
  connect(signalVoltage1.p,ground1.p) annotation(Line(points = {{-41.9801,4.15136},{-42.132,4.15136},{-42.132,-16.2437},{10.9074,-16.2437},{10.9074,-16.1522}}));
  connect(resistor1.n,inductor1.p) annotation(Line(points = {{-3.81545,53.3825},{9.13706,53.3825},{9.13706,53.3711},{9.16188,53.3711}}));
  connect(signalVoltage1.n,resistor1.p) annotation(Line(points = {{-41.9801,28.1514},{-42.132,28.1514},{-42.132,53.5533},{-27.8154,53.5533},{-27.8154,53.3825}}));
  connect(step1.y,signalVoltage1.v) annotation(Line(points = {{-66.2773,16.2338},{-52.0305,16.2338},{-52.0305,16.1514},{-50.3801,16.1514}}));
end dcmotor;

