# Write a program to find all words that can be reduced in this way, and then find the longest one.

def create_dict(filename):
    """ reads words from file
    
    returns a dictionary with words as key
    """

    d = {}

    for word in open(filename, 'r'):
        d[word.strip()] = []

    return d


def add_word_lists(d):
    """ adds list of words to dictionary """

    for word in d.keys():
        for i in range(len(word)):
            new = word.replace(word[i], '')
            if new in d:
                d[word].append(new)

    return d

def word_in_word(d):
    """ takes dict as argument and returns dict of lists """

    known = {'': [''], 'i': [''], 'a': ['']}
    l = []
    
    for word in d:
        if len(d[word]) < 1:
            continue

        for s in d[word]:
            if s in known:
                t = known[s].insert(0, s)
            else:
                return word_in_word(d)
    
            l.append(t)
    
        d[word] = max(l)

    return d


filename = 'words.txt'
d = (add_word_lists(create_dict(filename)))

"""
for key, values in d.items():
    if len(values) > 4:
        print(key, values)
"""
word_in_word(d)