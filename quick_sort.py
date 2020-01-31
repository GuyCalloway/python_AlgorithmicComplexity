import math


def pivot_splitter(arr):
    pivot = arr[0]
    above = []
    below = []

    for number in arr[1:]:
        if number > pivot:
            above.append(number)
        else:
            below.append(number)
    return (below, above, pivot)


def quicksort(arr):
    if len(arr) < 2:
        return arr
    (below, above, pivot) = pivot_splitter(arr)
    sorted_left = quicksort(below)
    sorted_right = quicksort(above)
    result = []
    result.extend(sorted_left)
    result.append(pivot)
    result.extend(sorted_right)
    return result
