import math


class MergeSort:
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

    def splitter(self, arr):
        res = []
        segments = int(math.ceil(len(arr)/2))
        x = 0
        for _ in range(segments):
            res.append(arr[int(math.floor(((x/segments) * len(arr)))):int(math.floor(((x+1)/segments)*len(arr)))])
            x += 1
        return res

    def sort_couples(self, z):
        for x in z:
            if (len(x) == 2):
                if x[0] > x[1]:
                    x[0], x[1] = x[1], x[0]

    def merge(self, z):
        i = 0
        res2 = []
        for _ in range(int(math.ceil(len(z)/2))):
            if i < len(z)-1:
                res2.append(self.merge_2_sorted_arrays(z[i], z[i+1]))
                i += 2
            else:
                res2.append(z[i])
        return res2

    def sort(self, array):
        result = self.splitter(array)
        self.sort_couples(result)
        while len(result) != 1:
            result = self.merge(result)
        return result[0]


if __name__ == "__main__":
    assert(merge_2_sorted_arrays(
        [2, 5, 7], [1, 2, 8, 9]) == [1, 2, 2, 5, 7, 8, 9])
    assert(sort([2, 5, 7, 2, 3, 6, 4]) == [2, 2, 3, 4, 5, 6, 7])
