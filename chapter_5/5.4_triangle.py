# determines whether triangle can be formed from three sticks

def is_triangle(a, b, c):
    """ takes three lengths as input and tests whether triangle can be formed """
    if ((a + b < c) or (a + c < b) or (b + c < a)):
        print('No')
    else:
        print('Yes')
        
# get input from user
a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))

# call function to check
is_triangle(a, b, c)