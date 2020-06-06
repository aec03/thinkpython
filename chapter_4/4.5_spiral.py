# a program that draws an Fibonacci spiral
from math import pi, radians
from swampy.TurtleWorld import TurtleWorld, Turtle, fd, lt, bk, rt

def fibonacci(f):
    """ calculate fibonacci number """
    a = f - 1
    b = f - 2

    if f == 0:
        return 0
    elif f == 1:
        return 1

    return fibonacci(a) + fibonacci(b)


def draw_fib(t, f):
    """ draws fibonacci spiral """
    for i in range(1, f + 1):
        if i == 0:
            continue
        else:
            q_circle(t, (fibonacci(i)))


def q_circle(t, r):
    """ draws quarter-circle """
    circumference = 2 * r * pi

    for _ in range(int(circumference / 4)):
        fd(t, 1)
        lt(t, 360 / circumference)


world = TurtleWorld()
bob = Turtle()
bob.delay = 0.02
rt(bob, 90)

# call fibonacci function with final fibonacci value
draw_fib(bob, 20)