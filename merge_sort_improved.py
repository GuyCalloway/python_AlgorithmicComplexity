import math


def merge_2_sorted_arrays(arr1, arr2):
    len1 = len(arr1)
    len2 = len(arr2)
    i, j = 0, 0
    result = []
    while i < len1 and j < len2:
        if arr1[i] < arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1

    while len1 > i:
        result.append(arr1[i])
        i += 1
    while len2 > j:
        result.append(arr2[j])
        j += 1
    return(result)


def splitter(arr):
    left = arr[:int(len(arr)/2)]
    right = arr[int(len(arr)/2):]
    return (left, right)


def sort(arr):
    if len(arr) < 2:
        return arr
    (left, right) = splitter(arr)
    sorted_left = sort1(left)
    sorted_right = sort1(right)
    return merge_2_sorted_arrays(sorted_left, sorted_right)
