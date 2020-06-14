import string
import random

def read_text(filename):
    t = []
    with open(filename) as file:
        for line in file:
            t += read_line(line)

    return t


def read_to_hist(t, num=2):
    h = dict()
    for i in range(len(t)):
        if i >= len(t) - num - 1:
            continue
        else:
            prefix = ' '.join(t[i:i + num])
            suffix = t[i + num + 1]
            if prefix not in h:
                h[prefix] = [suffix]
            else:
                h[prefix].append(suffix)

    return h


def read_line(line):
    line = line.replace('-', '')
    line = line.strip()
    return line.split()


def prefix_list(h):
    t = []
    for prefix in h:
        t.append(prefix)

    return t


def generate_suffix(prefix, h):
    return random.choice(h[prefix])


t = read_text('emma.txt')
h = read_to_hist(t, 2)
l = prefix_list(h)
