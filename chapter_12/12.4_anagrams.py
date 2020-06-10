#  Write a program that reads a word list from a file (see Section 9.1) and prints all the sets of words that are anagrams

def order_word(s):
    """ takes string and returns string with order characters """
    t = []
    word = ''

    for c in s:
        t.append(c)  
    
    t.sort()
    for c in t:
        word += c
    
    return word


def sort_dict(d):
    t = []

    for k, p in d.items():
        t.append((len(p), k))

    t.sort(reverse=True)

    l = []
    for _, key in t:
        l.append(key)

    return l


def scrabble(d):
    """ takes dict and returns word with 8 characters and most anagrams """
    for i in sort_dict(d):
        if len(i) >= 8:
            return i


words = {}

with open('words.txt') as file:

    for line in file:
        word = line.strip()
        
        string = order_word(word)

        if string in words:
            words[string].append(word)
        else:
            words[string] = [word]


for k, p in words.items():
    if len(k) >= 8:
        print(k)

top_scrabble = scrabble(words)
print(top_scrabble)
print(words[top_scrabble])