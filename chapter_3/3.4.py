# create a program that prints a string out four times using multiple functions

def do_four(f, x):
# called function twice and sets x as argument of function
    f(x)
    f(x)

def print_twice(word):
# prints argument string twice
    print(word)
    print(word)

# calls the do_four function
do_four(print_twice, "word")