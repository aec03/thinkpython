# use a dictionary to improve speed of fibonacci function

import time

known = {0: 0, 1: 1}

def fibonacci(n):
    if n in known:
        return known[n]

    res = fibonacci(n - 1) + fibonacci(n - 2)
    known[n] = res
    return res


def fibonacci_og(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_og(n-1) + fibonacci_og(n-2)


n = 100

start = time.time()
print(fibonacci(n))
end = time.time()
print(end - start)
print()

start2 = time.time()
print(fibonacci_og(n))
end2 = time.time()
print(end2 - start2)