# Write a function called rotate_word that takes a string and an integer as parameters, and that returns a new string that contains the letters from the original string “rotated” by the given amount.

def rotate_word(s, n):
    word = ''
    for c in s:
        if c.isupper():
            letter = chr((((ord(c) - 65) + n) % 26) + 65)
        elif c.islower():
            letter = chr((((ord(c) - 97) + n) % 26) + 97)
        else:
            letter = c

        word = word + letter

    return word

print(rotate_word('melon', -10))