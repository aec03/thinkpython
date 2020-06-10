# read words into dictionary

words = {}

with open('words.txt') as file:
    for line in file:
        word = line.strip()
        words[word] = ''

# test if word is in dictionary
word = 'helloo'
if word in words:
    print('True')
else:
    print('False')