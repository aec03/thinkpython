# evaluates palibdromes

def is_palindrome(word):
    if len(word) <= 2:
        return first(word) == last(word)

    if ((first(word) == last(word)) and (is_palindrome(middle(word)))):
        return True
    else:
        return False


def first(word):
    return word[0]


def last(word):
    return word[-1]


def middle(word):
    return word[1:-1]

# modified to accept sentences with non-alphabetic characters
string = 'Never odd or even.'
string = ''.join(x for x in string if x.isalpha())

print(is_palindrome(string.lower()))