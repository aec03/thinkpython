# Write a function called eval_loop that iteratively prompts the user, takes the resulting input and evaluates it using eval, and prints the result.

def eval_loop():
    while True:
        a = input('> ')
        if a == 'done':
            break
        else:
            print(eval(a))


eval_loop()