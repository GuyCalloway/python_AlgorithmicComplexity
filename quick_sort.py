import math


def q_splitter(arr):
    j = len(arr)-1
    i = 1

    while i != j:
        print(arr)
        if arr[0] >= arr[i]:
            i += 1
        if arr[0] <= arr[j]:
            j -= 1

        if arr[i] >= arr[0] and arr[j] <= arr[0]:
            arr[i], arr[j] = arr[j], arr[i]

    return arr[1:i], arr[i+1:], arr[0]


def quicksort(arr):
    print(arr)
    if len(arr) < 2:
        return arr
    (left, right, pivot) = q_splitter(arr)
    sorted_left = quicksort(left)
    sorted_right = quicksort(right)
    result = []
    result.extend(sorted_left)
    result.append(pivot)
    result.extend(sorted_right)
    print(result)
    return result
