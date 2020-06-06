# check Fermat's last theorem that (a^n + b^n = c^n) for n values > 2

def check_fermat(a, b, c, n):
    """ checks fermats last theorem """
    if ((a ^ n + b ^ n) == c ^ n):
        if n > 2:
            print("Holy smokes, Fermat was wrong!")
    else:
        print("No, does not work.")

# prompts users for values
a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))
n = int(input('n: '))

# calls check function
check_fermat(a, b, c, n)