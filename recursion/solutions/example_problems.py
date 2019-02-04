"""
This assignment is a variety of small problems to begin you getting used to the idea of recursion. They are not
full-blown interview questions, but do serve as a great start for getting your mind "in the zone" for recursion
problems.

Here are the solutions with some simple explanations to the problems.

______
### Problem 1

**Write a recursive function which takes an integer and computes the cumulative sum of 0 to that integer**

**For example, if n=4 , return 4+3+2+1+0, which is 10.**

This problem is very similar to the factorial problem presented during the introduction to recursion. Remember, always
think of what the base case will look like. In this case, we have a base case of n =0 (Note, you could have also
designed the cut off to be 1).

In this case, we have:
   n + (n-1) + (n-2) + .... + 0
"""


def rec_sum(n):
    # base case
    if n == 0:
        return 0
    else:
        return n + rec_sum(n - 1)


n = 10
print("rec_sum(" + str(n) + ") = " + str(rec_sum(n)))


"""
### Problem 2

**Given an integer, create a function which returns the sum of all the individual digits in that integer. For example:
if n = 4321, return 4+3+2+1**
"""


def sum_func(n):
    if len(str(n)) == 1:
        # base case
        return n
    else:
        return n % 10 + sum_func(n // 10)


n = 55
print("sum_func(" + str(n) + ") = " + str(sum_func(n)))


"""
### Problem 3
*Note, this is a more advanced problem than the previous two! It aso has a lot of variation possibilities and we're 
ignoring strict requirements here.*

Create a function called word_split() which takes in a string **phrase** and a set **list_of_words**. The function will 
then determine if it is possible to split the string in a way in which words can be made from the list of words. You 
can assume the phrase will only contain words found in the dictionary if it is completely splittable.
"""


