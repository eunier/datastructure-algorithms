"""
# Sentence Reversal

## Problem

Given a string of words, reverse all the words. For example:

Given:

    'This is the best'

Return:

    'best the is This'

As part of this exercise you should remove all leading and trailing whitespace. So that inputs such as:

    '  space here'  and 'space here      '

both become:

    'here space'
"""


def rev_words(string):
    length = len(string)
    words = []

    i = 0
    while i < length:
        if string[i] != ' ':
            word_start = i

            while i < length and string[i] != ' ':
                i += 1

            words.append(string[word_start:i])
        else:
            i += 1

    return " ".join(reversed(words))



print(rev_words("  Hello John      how are you"))
