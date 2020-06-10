# Write a function called sumall that takes any number of arguments and returns their sum

def sumall(*args):
    sum = 0

    for num in args:
        sum += num
    
    return sum


print(sumall(1, 2, 3, 4, 5))