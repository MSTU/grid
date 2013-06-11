<Qucs Schematic 4.4.0>
<Properties>
  <View=0,22,800,800,1,0,0>
  <Grid=10,10,1>
  <DataSet=grid_pareto_1.dat>
  <DataDisplay=grid_pareto_1.dpl>
  <OpenDisplay=1>
  <showFrame=0>
  <FrameText0=\x041D\x0430\x0437\x0432\x0430\x043D\x0438\x0435>
  <FrameText1=\x0427\x0435\x0440\x0442\x0438\x043B:>
  <FrameText2=\x0414\x0430\x0442\x0430:>
  <FrameText3=\x0412\x0435\x0440\x0441\x0438\x044F:>
</Properties>
<Symbol>
</Symbol>
<Components>
  <multi.Variable x 1 80 190 -51 29 0 0 "x" 0 "0.0" 0 "1" 0 "10" 0>
  <multi.Variable y 1 90 290 -51 29 0 0 "y" 0 "0.0" 0 "-5" 0 "5" 0>
  <grid.Pareto Pareto1 1 290 230 -51 29 0 0 "lc1,lc2" 0 "x,y" 0 "6" 0>
  <Data Data1 1 150 50 -38 21 0 0 "import grid.tests.test_lib as test_lib\n\n" 0>
  <grid.Loadcase lc1 1 290 100 -51 29 0 0 "" 0 "" 0 "test_lib.f1" 0 "[]" 0 "Python" 0 "%" 0 "%" 0 "" 0>
  <grid.Loadcase lc2 1 380 100 -51 29 0 0 "" 0 "" 0 "test_lib.f2" 0 "[]" 0 "Python" 0 "%" 0 "%" 0 "" 0>
</Components>
<Wires>
</Wires>
<Diagrams>
</Diagrams>
<Paintings>
</Paintings>
