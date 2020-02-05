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


def qsort_in_one(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        more = [i for i in arr[1:] if i > pivot]
        return qsort_in_one(less) + [pivot] + qsort_in_one(more)


print(quicksort([10, 5, 2, 3]))

print(qsort_in_one([10, 5, 2, 3]))
