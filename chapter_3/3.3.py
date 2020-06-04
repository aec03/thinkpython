# Write a function named right_justify that takes a string named s as a parameter and prints the string with enough leading spaces so that the last letter of the string is in column 70 of the display.


def right_justify(s):
# define fuction justify

    length = len(s)                 # get length of string
    spaces = 70 - length            # subtract length of string from 70

    print((' ' * spaces) + s)       # print the spaces and string

# call right_justify function
right_justify('aidan')