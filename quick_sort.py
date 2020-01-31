import math


def q_splitter(arr):
    value = arr[0]
    above = []
    below = []

    for number in arr[1:]:
        if number > value:
            above.append(number)
        else:
            below.append(number)
    return (below, above, value)


def quicksort(arr):
    if len(arr) < 2:
        return arr
    (left, right, pivot) = q_splitter(arr)
    sorted_left = quicksort(left)
    sorted_right = quicksort(right)
    result = []
    result.extend(sorted_left)
    result.append(pivot)
    result.extend(sorted_right)
    return result
