import math

focal_length = 600
diamiter = 150
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


def finishing():
    print(  "(Fine Grinding mirror with sagitta=%.3f)" % sagitta)
    print( "G0 X0.000 Y0.000 Z5.000")

    z = 0
    base_radius = diamiter / 2

    while True:
        base_radius -= radius_increment_fine
        if base_radius <= 0:
            break

        z = -(sagitta - base_radius*base_radius / (4 * focal_length))
        x = base_radius
        print(  "G0 X-%.3f" %x,  " Y0 ", "Z%.3f" %z)
        print(  "G02 X-%.3f" %x,  " Y0 ", "I%.3f" %x, " J0 F%.1f" % feed_rate)


#Send g-code header        
print( "G17 G90 G21 G54")

hogging()
finishing()



