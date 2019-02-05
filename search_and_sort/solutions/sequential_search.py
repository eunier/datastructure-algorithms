def seq_search(arr, item):
    pos = 0
    found = False

    while pos < len(arr) and not found:
        if arr[pos] == item:
            found = True
        else:
            pos += 1

    return found


def ordered_seq_search(arr_ordered, item):
    """
    Input array must be ordered / sorted
    """
    pos = 0
    found = False
    stopped = False

    while pos < len(arr_ordered) and not found and not stopped:
        if arr_ordered[pos] == item:
            found = True
        else:
            if arr[pos] > item:
                stopped = True
            else:
                pos += 1

    return found


arr = [1, 2, 3, 4, 5]
print(seq_search(arr, 2))
print(seq_search(arr, 6))
print(ordered_seq_search(arr, 3))
print(ordered_seq_search(arr, 6))
