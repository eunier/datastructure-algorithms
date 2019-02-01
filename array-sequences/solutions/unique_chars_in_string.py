"""
# Unique Characters in String

## Problem
Given a string,determine if it is compreised of all unique characters. For example, the string 'abcde' has all unique
characters and should return True. The string 'aabcde' contains duplicate characters and should return false.
"""


def uni_chars(s):
    # edge case
    if len(s) == 1:
        return True

    chars = set()

    for letter in s:
        if letter in chars:
            return False
        else:
            chars.add(letter)

    return True


print(uni_chars("abc"))
print(uni_chars("aabbcc"))
