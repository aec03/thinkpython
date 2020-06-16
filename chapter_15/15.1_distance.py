# Write a function called distance_between_points that takes two Points as arguments and returns the distance between them

import math

class Point(object):
    """ represents a point in a 2d space """

def distance_between_points(p1, p2):
    return math.sqrt((p2.x - p1.x)**2 + (p2.y - p1.y)**2)

p1 = Point()
p1.x = 0.0
p1.y = 0.0

p2 = Point()
p2.x = 4.0
p2.y = 4.0

print(distance_between_points(p1, p2))