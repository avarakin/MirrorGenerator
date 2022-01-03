(Exported by FreeCAD)
(Post Processor: grbl_post)
(Output Time:2021-12-31 16:26:05.414058)
(Begin preamble)
G17 G90
G21
(Begin operation: Fixture)
(Path: Fixture)
G54
(Finish operation: Fixture)
(Begin operation: T1: 1/8")
(Path: T1: 1/8")
(T1: 1/8")
(Begin toolchange)
( M6 T1.0 )
M3 S0.0
(Finish operation: T1: 1/8")
(Begin operation: Profile)
(Path: Profile)
(Profile)
(Compensated Tool Path. Diameter: 3.17)
G0 Z5.000
G0 X0.112 Y0.111
G0 Z3.000
G1 X0.112 Y0.111 Z-1.000 F180.000
G2 X0.075 Y-0.138 Z-1.000 I-0.111 J-0.111 K0.000 F1200.000
G1 X0.047 Y-0.150 Z-1.000 F1200.000
G2 X-0.048 Y0.149 Z-1.000 I-0.046 J0.150 K0.000 F1200.000
G2 X0.112 Y0.111 Z-1.000 I0.049 J-0.149 K0.000 F1200.000
G0 Z5.000
G0 Z5.000
(Finish operation: Profile)
(Begin operation: Profile001)
(Path: Profile001)
(Profile001)
(Compensated Tool Path. Diameter: 3.17)
G0 Z5.000
G0 X55.002 Y55.002
G0 Z3.000
G1 X55.002 Y55.002 Z-1.000 F180.000
G2 X3.777 Y-77.693 Z-1.000 I-55.002 J-55.002 K0.000 F1200.000
G2 X-77.693 Y-3.777 Z-1.000 I-3.777 J77.693 K0.000 F1200.000
G2 X-3.777 Y77.693 Z-1.000 I77.693 J3.777 K0.000 F1200.000
G2 X55.002 Y55.002 Z-1.000 I3.777 J-77.693 K0.000 F1200.000
G0 Z5.000
G0 Z5.000
(Finish operation: Profile001)
(Begin postamble)
M5
G17 G90
M2
