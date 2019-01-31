"""
# Anagram Check

## Problem

Given two strings, check to see if they are anagrams. An anagram is when the two strings can be written using the exact same letters (so you can just rearrange the letters to get a different phrase or word).

For example:

    "public relations" is an anagram of "crap built on lies."

    "clint eastwood" is an anagram of "old west action"

**Note: Ignore spaces and capitalization. So "d go" is an anagram of "God" and "dog" and "o d g".**
"""


def anagram_naive(s1, s2):
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()

    return sorted(s1) == sorted(s2)


def anagram(s1, s2):
    # remove whitespaces and set all letters to lowercase
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()

    # edge case check
    if len(s1) != len(s2):
        return False

    """
    Count the frequency of each letter, 
    if it is the same strings are anagrams
    """
    # this is a dictionary
    count = {}

    # fill the dictionary counting the frequency of each letter in s1
    for letter in s1:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1

    # subtract the frequency of each letter in the dictionary
    for letter in s2:
        if letter in count:
            count[letter] -= 1
        else:
            count[letter] = 1

    # if each value is 0 then strings are anagram
    for k in count:
        if count[k] != 0:
            return False

    return True


print(anagram_naive('god', 'dog'))
print(anagram('a b c', 'cba'))
