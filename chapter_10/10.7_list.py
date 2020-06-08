# Write a function called is_anagram that takes two strings and returns True if they are anagrams.

def is_anagram(s1, s2):
    s1 = list(s1.lower())
    s2 = list(s2.lower())

    if len(s1) != len(s2):
        return False

    s1.sort()
    s2.sort()

    for i in range(len(s1)):
        if s1[i] != s2[i]:
            return False

    return True


print(is_anagram('nadin', 'aidan'))