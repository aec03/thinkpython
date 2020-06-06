# draws flowers with turtle
import math
from swampy.TurtleWorld import TurtleWorld, Turtle, fd, lt, bk, rt


def arc(t, r, a):
    """ draws arc of circle from
    t: turtle
    r: radius of circle
    a: arc length """

    fraction = a/360
    circumference = 2 * r * math.pi

    length = int(fraction * circumference)

    for _ in range(length):
        fd(t, 1)
        lt(t, 360 / circumference)


def petal(t, r, a):
    """ draws petal from

    t: turtle
    r: radius of circle
    a: angle of arc """

    arc(t, r, a)
    lt(t, (180 - a))
    arc(t, r, a)
    lt(t, (180 - a))


def flower(t, r, a, n):
    """ draws flower from

    t: turtle
    r: radius of circle
    a: angle of arc
    n: number of petals """

    for _ in range(n):
        petal(t, r, a)                      # calls petal function
        lt(t, ((360 / n)))        # turns to make next petal


world = TurtleWorld()
bob = Turtle()
bob.delay = 0.01

# creates flower from givern turtle, radius, angle, number of petals
flower(bob, 180, 40, 10)