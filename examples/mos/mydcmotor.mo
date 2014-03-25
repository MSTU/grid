model dcmotor
  Modelica.Electrical.Analog.Basic.Resistor     resistor1(R = 10); 
  Modelica.Electrical.Analog.Basic.Inductor     inductor1(L = 0.2);
  Modelica.Electrical.Analog.Basic.Ground       ground1;
  Modelica.Electrical.Analog.Basic.EMF          emf1;
  Modelica.Electrical.Analog.Sources.SignalVoltage signalVoltage1;
  Modelica.Mechanics.Rotational.Components.Inertia      load(J = 1);    // Modelica version 3.1
  Modelica.Blocks.Sources.Step                  step1;
equation
  connect(step1.y, signalVoltage1.v);
  connect(signalVoltage1.p, resistor1.p);
  connect(resistor1.n, inductor1.p);
  connect(inductor1.n, emf1.p);
  connect(emf1.flange, load.flange_a); // Modelica version 3.1
  connect(signalVoltage1.n, ground1.p);
  connect(ground1.p, emf1.n);
end dcmotor;
