# Write a function called is_anagram that takes two strings and returns True if they are anagrams.

def is_anagram(s1, s2):
    if len(s1) != len(s2):
        return False

    for i in s1.lower():
        if i not in s2.lower():
            return False

    return True


print(is_anagram('aaida', 'aidan'))