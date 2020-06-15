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
    for i in range(len(t) - num):
        prefix = ' '.join(t[i:i + num])
        suffix = t[i + num]
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


def generate_prefix(t, num):
    while True:
        i = random.randint(1, len(t))
        if t[i][-1] == '.' and t[i + num][0].isupper():
            return t[i + num]


def generate_suffix(prefix, h):
    if prefix in h:
        return random.choice(h[prefix])
    else:
        return None


def generate_text(h, t, num=2):
    prefix = generate_prefix(t, num)
    sentence = prefix + ' '
    while True:
        suffix = generate_suffix(prefix, h)
        if (suffix == None or suffix[-1] == '.') and (suffix != 'Mr.' and suffix != 'Mrs.'):
            sentence += suffix
            break
        else:
            sentence += suffix + ' '
            sentence.strip()
            sen = sentence.split()
            prefix = ' '.join(sen[-num:])
    
    return sentence


num = 3
t = read_text('emma.txt')
h = read_to_hist(t, num)
t = prefix_list(h)
print(generate_text(h, t, num))