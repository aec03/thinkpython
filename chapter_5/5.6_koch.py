from swampy.TurtleWorld import *

def koch(t, x):
    """ draw koch curve """
    if x < 4:
        fd(t, x)
    else:
        koch(t, x / 4)
        lt(t, 90)
        koch(t, x / 4)
        rt(t, 90)
        koch(t, x / 4)
        rt(t, 90)
        koch(t, x / 4)
        lt(t, 90)
        koch(t, x / 4)


def snowflake(t, x):
    for _ in range(3):
        koch(t, x)
        rt(t, 120)
    

world = TurtleWorld()
bob = Turtle()
bob.delay = 0.01

koch(bob, 100)