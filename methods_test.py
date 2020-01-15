import unittest
from methods import Methods
from merge_sort import MergeSort
from merge_sort_improved import sort


class TestMethods(unittest.TestCase):
    def test_if_method_merges_two_sorted_arrays(self):
        Methods = MergeSort()
        list1 = [1, 2, 1, 11, 6, 5, 7, 10, 5, 4, 3, 5, 6, 11]
        self.assertEqual(Methods.sort(list1), [
                         1, 1, 2, 3, 4, 5, 5, 5, 6, 6, 7, 10, 11, 11])

    def test_if_method_reverses_string(self):
        list1 = [5, 1, 2, 3, 1, 4, 5, 5, 6, 4, 7]
        self.assertEqual(Methods.reverse(list1), [
                         7, 4, 6, 5, 5, 4, 1, 3, 2, 1, 5])

    def test_if_counts_number_of_duplicatesDOUBLESONLY(self):
        list1 = [5, 1, 2, 3, 1, 4, 5, 5, 6, 4, 7]
        self.assertEqual(Methods.find_duplicates(list1), [1, 4])

    def test_if_shuffles_list(self):
        list1 = [5, 1, 2, 3, 10, 1, 4, 5, 5, 6, 4, 7, 10]
        self.assertNotEqual(Methods.shuffle3(list1), [
                            5, 1, 2, 3, 10, 1, 4, 5, 5, 6, 4, 7, 10])
        self.assertEqual(len(Methods.shuffle3(list1)), len(list1))

    def test_find_most_feq_val(self):
        list1 = [5, 1, 2, 3, 3, 3, 1, 4, 5, 5, 6, 4, 4, 7]
        self.assertEqual(Methods.find_most_freq_values(list1), [5, 3, 4])

    def test_sortit(self):
        list1 = [5, 1, 2, 3, 3, 3, 1, 4, 5, 5, 6, 4, 4, 7]
        list2 = [5, 3, 1, 1, 1, 8, 8, 8, 9, 7, 3, 1, 1, 1]
        self.assertEqual(Methods.sortit2(list1), [
                         1, 1, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 7])
        self.assertEqual(Methods.sortit2(list2), [
                         1, 1, 1, 1, 1, 1, 3, 3, 5, 7, 8, 8, 8, 9])

    def test_sort0n1s(self):
        list1 = [0, 1, 1, 0, 0, 0, 1, 0, 1, 0]
        self.assertEqual(Methods.sort0n1s(list1), [
                         0, 0, 0, 0, 0, 0, 1, 1, 1, 1])

    def test_mecha_coach(self):
        list1 = ["Alice", "Bob", "Charly", "Dan"]
        self.assertEqual(Methods.mecha_coach(list1), [
            [["Alice", "Bob"], ["Charly", "Dan"]],
            [["Alice", "Charly"], ["Bob", "Dan"]],
            [["Alice", "Dan"], ["Bob", "Charly"]],
        ])

    def test_fibonacci(self):
        self.assertEqual(Methods.fibonacci(1), [0])
        self.assertEqual(Methods.fibonacci(0), [])
        self.assertEqual(Methods.fibonacci(2), [0, 1])
        self.assertEqual(Methods.fibonacci(3), [0, 1, 1])
        self.assertEqual(Methods.fibonacci(7), [0, 1, 1, 2, 3, 5, 8])

    # def test_quick_sort(self):
    #     Methods = QuickSort()
    #     self.assertEqual(Methods.pivot([5, 7, 5, 7, 1, 7, 6, 532, 2, 6, 7, 7, 5]), [
    #         2, 1, 4, 3, 5, 8, 7, 9, 6])


if __name__ == '__main__':
    unittest.main()
