# Write a function called has_duplicates that takes a list and returns True if there is any element that appears more than once

from random import randint

def birthday():
    """ generate a random birthday

        returns a list w two objects:
         - a month
         - a year """

    return [randint(1, 13), randint(1, 31)]

def birthday_list(n):
    """ generates a list of birthdays"""
    t = []

    for _ in range(n):
        t.append(birthday())

    return t

def has_duplicates(t, n):
    """ checks whether their are duplicate birthdays in list """

    for i in range(n):
        counter = 0

        for j in range(n):
            if (t[i][0] == t[j][0]) and (t[i][1] == t[j][1]):
                counter += 1
        
            if counter == 2:
                return True

    return False


n = 23
b = birthday_list(n)
print(has_duplicates(b, n))