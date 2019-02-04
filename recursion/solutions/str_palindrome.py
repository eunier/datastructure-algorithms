"""
Write a function that takes a string as a parameter and returns True if the string is a palindrome, False otherwise. 
Remember that a string is a palindrome if it is spelled the same both forward and backward. For example: radar is a 
palindrome. for bonus points palindromes can also be phrases, but you need to remove the spaces and punctuation before 
checking. for example: madam i’m adam is a palindrome. Other fun palindromes include:
"""


def pal(string):
    if len(string) <= 1:
        return True

    return (string[0] == string[-1]) and pal(string[1:-1])


# true
print(pal('abccba'))
print(pal('abcdcba'))
# false
print(pal('abcdef'))
print(pal('abcdefg'))
