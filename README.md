# Telescope Mirror Generator

This program generates g-code for rough grinding of a telescope mirror using CNC router. 
It can run in two modes:
1. Hogging, which takes material in multiple layers, each layer comprised of concentric circles with constant stepover
2. Fine grinding, which just removes material in one go using downward helix with constant stepover

Depending on the tool, feed speed, machine and mirror parameters, step #1 may be skipped.

Please note that this toolpath will produce a parabolic shape.


MirrorGenerator.py has input parameters at the top of the file to configure the job parameters. It just spits out the g-code to the console, you need to capture it into file using file redirection:

```
python MirrorGenerator.py > mirror.gcode
```

This project also has couple of sample g code files:
```
mirror.gcode - rough grinding
mirror_helix.gcode - fine grinding using helix strategy
```
