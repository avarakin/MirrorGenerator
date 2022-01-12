# Telescope Mirror rough grinding using CNC router

This project describes the process of rough grinding of a telescope mirror using a CNC router
It provides guidance in terms of how to approach the process and also provides a g-code generator for toolpaths to grind the mirror. The following challenges had to be overcome as part of this process:
- Mirror holding
- Grinding tool selection
- Cooling of the tool and mirror
- Dust control
- Tool path generation using g-code

## Grinding tool
The tool needs to be low cost and at the same time provide decent longevity.
The following tool was selected and used for griding of test 6" mirror. The tool was is pretty good shape after grinding this mirror.
Name of the tool is: "uxcell Diamond Burrs Bits Grinding Drill Carving Rotary Tool for Glass Stone Ceramic 120 Grit 1/4" Shank 10mm Cylinder Ball Nose 5 Pcs", Amazon URL:
https://www.amazon.com/gp/product/B01GUHHQOO/ref=ppx_yo_dt_b_asin_title_o03_s00?ie=UTF8&psc=1



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
