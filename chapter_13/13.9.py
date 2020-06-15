# Write a program that reads a text from a file, counts word frequencies, and prints one line for each word, in descending order of frequency, with log f and log r

from matplotlib import pyplot as plt
import string
import math

# global variables
word_freq = {}
words = []
f = []
r = []

def read_text(filename):
    global word_freq
    with open(filename) as file:
        for line in file:
            read_line(line, word_freq)


def read_line(line, hist):
    line = line.replace('-', ' ')
    line = line.strip()
    
    for word in line.split():
        word = word.strip(string.punctuation).lower()
        if word in hist:
            hist[word] += 1
        else:
            hist[word] = 1


def word_list(h):
    global words
    for word, freq in h.items():
        f = math.log(freq)
        words.append([f, word])

    words.sort(reverse=True)
    for i in range(len(words)):
        words[i].append(math.log(i + 1))


def freq_list(t):
    global f, r
    for freq, _, rank in t:
        f.append(freq)
        r.append(rank)


filename = 'emma.txt'
read_text(filename)
word_list(word_freq)
freq_list(words)

plt.plot(r, f)
plt.show()