#this program generates code for grinding a parabolic mirror
#Initial formula used is y^2 = 4ax
#It can be converter to x^2 = 4az or x = sqrt (4az)

import math


focal_length = 600
diamiter = 150
depth_of_cut = 0.1
radius_increment = 2
sagitta = (diamiter/2)*(diamiter/2) / (4 * focal_length)

#hogging steps - for each depth of cut we have to run concentric circles to remove the material
z = 0
while True:
    radius = math.sqrt (4*focal_length* (sagitta - z))
    x = radius
    print(  "z=%.3f" % z, "x=%.3f" % x)
    while True:
        x -= radius_increment
        if x < 0 :
            break
    z += depth_of_cut
    if z >= sagitta:
        break

print(  "sagitta=%.3f" % sagitta)

#fine grinding steps - we need to shape the form, no concentric circles needed here, because all the material was removed as part of hogging steps
