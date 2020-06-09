# Write a function called is_sorted that takes a list as a parameter and returns True if the list is sorted in ascending order and False otherwise

def is_sorted(t):
    orig = t[:]
    t.sort()
    for i in range(len(orig)):
        if orig[i] != t[i]:
            return False

    return True


t = ['z', 'b', 'c', 's', 'x']
print(is_sorted(t))