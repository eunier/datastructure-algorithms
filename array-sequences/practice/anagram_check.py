"""
# Anagram Check

## Problem

Given two strings, check to see if they are anagrams. An anagram is when the two strings can be written using the exact
same letters (so you can just rearrange the letters to get a different phrase or word).

For example:

    "public relations" is an anagram of "crap built on lies."

    "clint eastwood" is an anagram of "old west action"

**Note: Ignore spaces and capitalization. So "d go" is an anagram of "God" and "dog" and "o d g".**
"""


def anagram(s1, s2):
    s1 = str(s1).replace(' ', '').lower()
    s2 = str(s2).replace(' ', '').lower()

    if len(s1) != len(s2):
        return False

    freq = {}

    for letter in s1:
        if letter in freq:
            freq[letter] += 1
        else:
            freq[letter] = 1

    for letter in s2:
        if letter in freq:
            freq[letter] -= 1
        else:
            return False

    return True


print(anagram("1a b c1", "cba11"))
print(anagram("1a b c134234", "cba11"))
