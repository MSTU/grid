model Linear_actuator
  Modelica.Mechanics.Rotational.Sources.Torque torque1 annotation(Placement(visible = true, transformation(origin = {-9.20701,-49.1698}, extent = {{10,-10},{-10,10}}, rotation = 0)));
  Modelica.Blocks.Sources.Step step1(height = 10) annotation(Placement(visible = true, transformation(origin = {36.3467,-49.2894}, extent = {{10,-10},{-10,10}}, rotation = 0)));
  Modelica.Mechanics.Translational.Components.IdealGearR2T idealgearr2t1(ratio = 1) annotation(Placement(visible = true, transformation(origin = {-42.4666,66.4907}, extent = {{-10,-10},{10,10}}, rotation = 0)));
  Modelica.Mechanics.Rotational.Components.Inertia inertia2(J = 0.1) annotation(Placement(visible = true, transformation(origin = {-80.2096,46.9113}, extent = {{-10,-10},{10,10}}, rotation = 90)));
  Modelica.Mechanics.Rotational.Components.Inertia inertia1(J = 0.1) annotation(Placement(visible = true, transformation(origin = {-80.2395,-27.6446}, extent = {{-10,-10},{10,10}}, rotation = 90)));
  Modelica.Mechanics.Translational.Components.Fixed fixed1 annotation(Placement(visible = true, transformation(origin = {79.4643,66.578}, extent = {{-10,-10},{10,10}}, rotation = 0)));
  Modelica.Mechanics.Translational.Components.SpringDamper springdamper2(c = 20, d = 3, s_rel0 = 0) annotation(Placement(visible = true, transformation(origin = {42.142,66.1234}, extent = {{-10,-10},{10,10}}, rotation = 0)));
  Modelica.Mechanics.Translational.Components.Mass mass1(m = 0.5, L = 0) annotation(Placement(visible = true, transformation(origin = {0.570264,66.5351}, extent = {{-10,-10},{10,10}}, rotation = 0)));
  Modelica.Mechanics.Rotational.Components.SpringDamper springdamper1(c = 15, d = 2) annotation(Placement(visible = true, transformation(origin = {-80.5588,10.4773}, extent = {{-10,-10},{10,10}}, rotation = 90)));
equation
  connect(springdamper1.flange_b,inertia2.flange_a) annotation(Line(points = {{-80.5588,20.4773},{-80.5588,36.787},{-80.2096,36.787},{-80.2096,36.9113}}));
  connect(inertia1.flange_b,springdamper1.flange_a) annotation(Line(points = {{-80.2395,-17.6446},{-80.2395,-0.232829},{-80.5588,0.477299},{-80.5588,0.477299}}));
  connect(mass1.flange_b,springdamper2.flange_a) annotation(Line(points = {{10.5703,66.5351},{31.8976,66.5351},{32.142,66.8219},{32.142,66.1234}}));
  connect(idealgearr2t1.flangeT,mass1.flange_a) annotation(Line(points = {{-32.4666,66.4907},{-9.31315,66.4907},{-9.42974,66.3023},{-9.42974,66.5351}}));
  connect(springdamper2.flange_b,fixed1.flange) annotation(Line(points = {{52.142,66.1234},{80.0931,66.1234},{80.0931,66.578},{79.4643,66.578}}));
  connect(torque1.flange,inertia1.flange_a) annotation(Line(points = {{-19.207,-49.1698},{-80.326,-49.1698},{-80.326,-37.4854},{-80.326,-37.4854}}));
  connect(inertia2.flange_b,idealgearr2t1.flangeR) annotation(Line(points = {{-80.2096,56.9113},{-80.2096,66.5891},{-52.4666,66.5891},{-52.4666,66.4907}}));
  connect(step1.y,torque1.tau) annotation(Line(points = {{25.3467,-49.2894},{3.40681,-49.2894},{3.40681,-48.8978},{3.40681,-48.8978}}));
  annotation(Icon(coordinateSystem(extent = {{-100,-100},{100,100}}, preserveAspectRatio = true, initialScale = 0.1, grid = {2,2})), Diagram(coordinateSystem(extent = {{-100,-100},{100,100}}, preserveAspectRatio = true, initialScale = 0.1, grid = {2,2}), graphics = {Rectangle(extent = {{21.8437,-21.8437},{21.8437,-21.8437}})}));
end Linear_actuator;

