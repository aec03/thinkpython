# create a program that prints out a grid
# limited by not using for statements

def grid():
# function for creating grid
    row_divider()
    columns()
    columns()
    row_divider()
    columns()
    columns()
    row_divider()
    columns()
    columns()
    row_divider()
    columns()
    columns()
    row_divider()


def row_divider():
# function for creating row_dividers
    print('+ - - + - - + - - + - - +')


def columns():
# funtion for creating columns
    print('|     |     |     |     |')

# call grid function
grid()