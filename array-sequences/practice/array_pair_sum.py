"""# Array Pair Sum

## Problem

Given an integer array, output all the ** *unique* ** pairs that sum up to a specific value **k**.

So the input:

    pair_sum([1,3,2,2],4)

would return **2** pairs:

     (1,3)
     (2,2)

**NOTE: FOR TESTING PURPOSES CHANGE YOUR FUNCTION SO IT OUTPUTS THE NUMBER OF PAIRS**
"""


def pair_sum(arr, k):
    if len(arr) < 2:
        return

    seen = set()
    output = set()

    for n in arr:
        target = k - n

        if target not in seen:
            output.add((min(n, target), max(n, target)))
        else:
            seen.add(n)

    return '\n'.join(map(str, list(output)))


print(pair_sum([1, 3, 2, 2], 4))
