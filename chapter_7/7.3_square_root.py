# approximate square root function
from sys import float_info
import math

def square_root(a):
    """ square root function """
    x = 2
    while True:
        y = (x + a / x ) / 2
        if (abs(y - x) < (float_info.epsilon)):
            return y
        x = y

def test_square_root():
    """ prints out table to analysis square roots"""
    space = 20
    for i in range(1, 10):
        print(float(i), (' '), end='')
        print(square_root(i), ((space - len(str(square_root(i)))) * (' ')), end=''),
        print(math.sqrt(i), ((space - len(str(math.sqrt(i)))) * (' ')), end=''),
        print(abs(square_root(i) - math.sqrt(i)))

        ((space - len(str(square_root(i)))) * (' '))

test_square_root()