#this program generates code for grinding a parabolic mirror
#Initial formula used is y^2 = 4ax
#It can be converter to x^2 = 4az or x = sqrt (4az)

import math


focal_length = 600
diamiter = 150
radius_increment = 3
sagitta = (diamiter/2)*(diamiter/2) / (4 * focal_length)

#hogging steps - for each depth of cut we have to run concentric circles to remove the material
z = 0
base_radius = diamiter / 2

while True:
    base_radius -= radius_increment
    if base_radius <= 0:
        break

    z = sagitta - base_radius*base_radius / (4 * focal_length)
    print(  ";Processing slice z=%.3f" % z, "x=%.3f" % base_radius)
    x = base_radius
    while True:
        print(  "z=%.3f" % z, "x=%.3f" % x)
        x -= radius_increment
        if x < 0 :
            break
print(  "sagitta=%.3f" % sagitta)

#fine grinding steps - we need to shape the form, no concentric circles needed here, because all the material was removed as part of hogging steps
