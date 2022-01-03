import math

focal_length = 750
diamiter = 152.4
radius_increment = 4
radius_increment_fine = 0.5
sagitta = (diamiter/2)*(diamiter/2) / (4 * focal_length)
feed_rate = 1000


def hogging():
    print(  "(Hogging mirror with sagitta=%.3f)" % sagitta)
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



#def spiral(start_radius, end_radius, depth):
#    print( "G0 X0.000 Y0.000 Z5.000")    

def finishing():
    print(  "(Fine Grinding mirror with sagitta=%.3f)" % sagitta)

    base_radius = diamiter / 2

    print( "G0 X-%.3f" %base_radius, " Y0.000 Z0.000")

    z = 0



    while True:

        z_old = -(sagitta - base_radius*base_radius / (4 * focal_length))
        z = -(sagitta - (base_radius - radius_increment_fine )* (base_radius - radius_increment_fine ) / (4 * focal_length))
        z_delta = z - z_old

        xy_delta = radius_increment_fine  # * base_radius / (diamiter/2)
        

        x1 = 0 - xy_delta/4
        y1 = base_radius - xy_delta/4
        z1 = z_old + z_delta/4
        r1 = base_radius - xy_delta * 0.125
        print(  "G02 X%.3f" %x1,  " Y%.3f" %y1, " R%.3f" %r1, " Z%.3f" %z1, " F%.1f" % feed_rate)


        x2 = base_radius - xy_delta/2
        y2 = 0
        z2 = z_old + z_delta/2
        r2 = base_radius - xy_delta * 0.375
        print(  "G02 X%.3f" %x2,  " Y%.3f" %y2, " R%.3f" %r2, " Z%.3f" %z2, " F%.1f" % feed_rate)

        x3 = 0 # - xy_delta * 0.75
        y3 = -(base_radius - xy_delta*0.75)
        z3 = z_old + z_delta*0.75
        r3 = base_radius - xy_delta*0.625
        print(  "G02 X%.3f" %x3,  " Y%.3f" %y3, " R%.3f" %r3, " Z%.3f" %z3, " F%.1f" % feed_rate)

        x4 = -(base_radius - xy_delta)
        y4 = 0
        z4 = z_old + z_delta
        r4 = base_radius - xy_delta * 0.875
        print(  "G02 X%.3f" %x4,  " Y%.3f" %y4, " R%.3f" %r4, " Z%.3f" %z4, " F%.1f" % feed_rate)

        base_radius -= radius_increment_fine
#        if base_radius <= 0 :
        if base_radius <= radius_increment_fine :
            break



print( "G17 G90 G21 G54")
#hogging()
finishing()
