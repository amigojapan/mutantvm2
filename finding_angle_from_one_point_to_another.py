#this script is to know the math in finding the direction we should face to go to a point
import math
# point 1
x1 = 0
y1 = 0

# point 2
x2 = -10
y2 = 0

deltax = x2 - x1
deltay = y2 - y1

angle_rad = math.atan2(deltay,deltax)
angle_deg = angle_rad*180.0/math.pi

print "The angle is %.5f radians (%.5f degrees)." % (angle_rad,angle_deg)