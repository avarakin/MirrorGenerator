# Telescope Mirror Generator

This program generates g-code for rough grinding of a telescope mirror. 
It can run in two modes:
1. Hogging, which takes material in multiple layers, each layer comprised of concentric circles with constant stepover
2. Fine grinding, which just removes material in one go using concentric circles with constant stepover

Depending on the tool, feed speed, machine and mirror parameters, step #1 may be skipped.

Please note that this toolpath will produce a parabolic shape.
