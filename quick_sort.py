class QuickSort:
    def pivot(self, arr):
        j = len(arr)-1
        i = 1

        while i < j:
            if arr[0] <= arr[j]:
                j -= 1
            if arr[0] >= arr[i]:
                i += 1

            # if arr[i] == arr[0]:
            #     print('same')
            #     i += 1

            if arr[i] >= arr[0] and arr[j] <= arr[0]:
                arr[i], arr[j] = arr[j], arr[i]
        # arr[0], arr[i-1] = arr[i-1], arr[0]
        print(i)
        print(j)
        print(arr)

        return [arr, i]
