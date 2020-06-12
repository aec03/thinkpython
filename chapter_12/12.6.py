# Write a program to find all words that can be reduced in this way, and then find the longest one.

def create_dict(filename):
    """ reads words from file
    
    returns a dictionary with words as key
    """

    d = {}

    with open(filename) as file:

        for word in file:
            d[word.strip()] = []

        return d


def create_list(d):
    """ create sorted list from dict keys """
    t = []

    for i in d:
        t.append(i)

    return sorted(t, key=len)


def add_word_lists(d):
    """ adds list of words to dictionary """

    d[''] = []

    for word in d.keys():
        if len(word) == 1:
            d[word] = ['']

        else:
            for i in range(len(word)):
                new = word.replace(word[i], '')
                if new in d and new not in d[word]:
                    d[word].append(new)

    return d


def word_count(d, t):
    """ takes dict as argument and returns dict of lists """

    known = {'': 0, 'i': 1, 'a': 1}

    for word in t:
        l = []
        if len(d[word]) < 1:
            known[word] = 0
        else:
            for i in d[word]:
                l.append(1 + known[i])
            known[word] = max(l)

    return known
    

filename = 'words.txt'
d = create_dict(filename)
d = add_word_lists(d)
t = create_list(d)
d = word_count(d, t)


"""
for key, values in d.items():
    if len(values) > 4:
        print(key, values)
"""

print(d['time'])