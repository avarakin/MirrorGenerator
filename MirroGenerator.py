import math


focal_length = 600
diamiter = 150
radius_increment = 2
sagitta = (diamiter/2)*(diamiter/2) / (4 * focal_length)

feed_rate = 100


print(  "(Grinding mirror with sagitta=%.3f)" % sagitta)



print( "G17 G90 G21 G54")
print( "G0 X0.000 Y0.000 Z5.000")

#hogging steps - for each depth of cut we have to run concentric circles to remove the material
z = 0
base_radius = diamiter / 2

while True:
    base_radius -= radius_increment
    if base_radius <= 0:
        break

    z = -(sagitta - base_radius*base_radius / (4 * focal_length))
    print(  "(Processing slice z=%.3f" % z, "x=%.3f)" % base_radius)
    x = base_radius
    print(  "G0 X-%.3f" %x,  " Y0 ", "Z%.3f" %z)
    while True:
        print(  "G0 X-%.3f" %x,  " Y0 ", "Z%.3f" %z)
        print(  "G02 X-%.3f" %x,  " Y0 ", "I%.3f" %x, " J0 F%.1f" % feed_rate)
        x -= radius_increment
        if x < 0 :
            break


#TODO:  fine grinding steps - we need to shape the form, no concentric circles needed here, because all the material was removed as part of hogging steps


