from math import pi, radians
from swampy.TurtleWorld import *

world = TurtleWorld()
bob = Turtle()
bob.delay = 0.01


def square(t, length):
# draws square
    for i in range(4):
        fd(t, length)
        lt(t)


def polygon(t, length, sides):
# draws polygon
    for i in range(sides):
        fd(t, length)
        lt(t, 360 / sides)


def arc(t, radius, angle):
# draws circle
    fraction = angle/360
    circumference = 2 * radius * pi

    length = int(fraction * circumference)

    for i in range(length):
        fd(t, 1)
        lt(t, 360 / circumference)