# Write a function called estimate_pi that uses this formula to compute and return an estimate of π

import math

def estimate_pi():
    """ uses infinite series formula by Srinivasa Ramanujan to calculate pi """
    k = 0
    x = 0
    l = 0
    while True:
        # forumla to find 1 / pi
        y = ((((factorial(4 * k) * (1103 + (26390 * k))) * (2 * math.sqrt(2))) / (((factorial(k)** 4) * (396 ** (4 * k))) * 9801)))

        if abs(y - l) < (1e-15):
            return 1 / x

        k += 1
        x = x + y
        l = y


def factorial(x):
    """ calculates factorial of number """
    if x <= 1:
        return 1

    return x * factorial(x - 1)

# call function to calculate approximate value of 1/pi
print(estimate_pi())