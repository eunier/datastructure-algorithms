"""
# Largest Continuous Sum

## Problem
Given an array of integers (positive and negative) find the largest continuous sum.
"""


def max_sum_finder(arr):
    # edge case
    if len(arr) == 0:
        return 0

    max_sum = current_sum = arr[0]

    for num in arr[1:]:
        # check for max num
        current_sum = max(current_sum + num, num)
        max_sum = max(current_sum, max_sum)

    return max_sum


# 29
print(max_sum_finder([1, 2, -1, 3, 4, 10, 10, -10, -1]))
