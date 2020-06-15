import string
import random
import time

from bisect import bisect

def process_file(filename):
    hist = dict()
    with open(filename) as file:
        for line in file:
            process_line(line, hist)
        return hist


def process_line(line, hist):
    line = line.replace('-', ' ')

    for word in line.split():
        word = word.strip(string.punctuation + string.whitespace)
        word = word.lower()

        hist[word] = hist.get(word, 0) + 1


def total_words(hist):
    return sum(hist.values())


def different_words(hist):
    return len(hist)


def most_common(hist):
    t = []
    for key, value in hist.items():
        t.append((value, key))

    t.sort(reverse=True)
    return t


def print_most_common(hist, num=10):
    t = most_common(hist)
    print('The most common words are:')
    for freq, word in t[0:num]:
        print(word, '\t', freq)


def random_word(h):
    t = []
    for word, freq in h.items():
        t.extend([word] * freq)

    return random.choice(t)


def rand_word_list(h):
    t = []
    k = []
    for key, value in h.items():
        if len(t) < 1:
            t.append(value)
            k.append(key)
        else:
            t.append(value + t[-1])
            k.append(key)
    
    return (t, k)


def word_list(h):
    k = []
    for key in h:
        k.append(key)

    return k


def freq_list(h):
    t = []
    freq = 0
    for k in h:
        freq += h[k]
        t.append(freq)
    
    return t


def rand_word(t, k, n):
    """ personal random word generator """
    for _ in range(n):
        x = random.randint(1, t[-1])
        index = bisect(t, x)
        print(k[index])


def book_random(h):
    t = []
    for key in h:
        if len(t) > 1:
            t.append(h[key] + t[-1])
        else:
            t.append(h[key])


h = process_file('emma.txt')
print_most_common(h)
rand_word(freq_list(h), word_list(h), 5)