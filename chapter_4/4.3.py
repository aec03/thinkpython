# draws polygon pies with turtle
from math import sin, cos, radians
from swampy.TurtleWorld import TurtleWorld, Turtle, fd, lt, bk, rt

world = TurtleWorld()
bob = Turtle()


def polygon_pie(t, length, sides):
# draws polygon
    angle = (((sides - 2) * 180) / (sides * 2))         # gets interior angle of polygon and divides it by 2
    slice = ((length / 2) / cos(radians(angle)))        # gets length of interior dividers using cosine

    for _ in range(sides):
    # create triangle for each side in polygon
        fd(t, slice)
        lt(t, (180 - angle))
        fd(t, length)
        lt(t, (180 - angle))
        fd(t, slice)
        lt(t, 180)

# call polygon_pie function to
polygon_pie(bob, 100, 9)