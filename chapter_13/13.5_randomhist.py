# Write a function named choose_from_hist that takes a histogram as defined in Section 11.1 and returns a random value from the histogram, chosen with probability in proportion to frequency

import random

def choose_from_hist(h):
    t = []
    for item, hist in h.items():
        for _ in range(hist):
            t.append(item)

    return random.choice(t)


def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1

    return d


print(choose_from_hist(histogram('aidan')))