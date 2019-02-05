def bin_search(arr, item):
    first = 0
    last = len(arr) - 1
    found = False

    while first <= last and not found:
        mid = int((first + last) / 2)

        if arr[mid] == item:
            found = True
        else:
            if item < arr[mid]:
                last = mid - 1
            else:
                first = mid + 1

    return found


def rec_bin_search(arr, item):
    # best case
    if len(arr) == 0:
        return False
    else:
        mid = int(len(arr) / 2)

        if arr[mid] == item:
            return True
        else:
            if item < arr[mid]:
                return rec_bin_search(arr[:mid], item)
            else:
                return rec_bin_search(arr[mid + 1:], item)


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(bin_search(arr, 4))
print(bin_search(arr, 13))
print(rec_bin_search(arr, 4))
print(rec_bin_search(arr, 13))
