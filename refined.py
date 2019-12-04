class RefinedSort:
    def merge_2_sorted_arrays(self, arr1, arr2):
        len1 = len(arr1)
        len2 = len(arr2)
        i = 0
        j = 0
        k = 0
        result = [None] * (len1 + len2)
        while i < len1 and j < len2:
            if arr1[i] < arr2[j]:
                result[k] = arr1[i]
                i += 1
                k += 1
            else:
                result[k] = arr2[j]
                j += 1
                k += 1
        while len1 > i:
            result[k] = arr1[i]
            i += 1
            k += 1

        while len2 > j:
            result[k] = arr2[j]
            j += 1
            k += 1
        return(result)

    def split_array(arr):
