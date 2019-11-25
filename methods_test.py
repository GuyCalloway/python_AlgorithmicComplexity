import unittest
from methods import Methods


class TestMethods(unittest.TestCase):

    def test_if_method_reverses_string(self):
        result = Methods()
        list1 = [5, 1, 2, 3, 1, 4, 5, 5, 6, 4, 7]
        self.assertEqual(result.reverse(list1), [
                         7, 4, 6, 5, 5, 4, 1, 3, 2, 1, 5])

    def test_if_counts_number_of_duplicatesDOUBLESONLY(self):
        result = Methods()
        list1 = [5, 1, 2, 3, 1, 4, 5, 5, 6, 4, 7]
        self.assertEqual(result.find_duplicates(list1), [1, 4])

    def test_if_shuffles_list(self):
        result = Methods()
        list1 = [5, 1, 2, 3, 1, 4, 5, 5, 6, 4, 7]
        self.assertNotEqual(result.shuffle(list1), list1)
        self.assertEqual(len(result.shuffle(list1)), len(list1))

    def test_find_most_feq_val(self):
        result = Methods()
        list1 = [5, 1, 2, 3, 3, 3, 1, 4, 5, 5, 6, 4, 4, 7]
        self.assertEqual(result.find_most_freq_values(list1), [5, 3, 4])

    def test_sortit(self):
        result = Methods()
        list1 = [5, 1, 2, 3, 3, 3, 1, 4, 5, 5, 6, 4, 4, 7]
        list2 = [5, 3, 1, 1, 1, 8, 8, 8, 9, 7, 3, 1, 1, 1]
        self.assertEqual(result.sortit2(list1), [
                         1, 1, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 7])
        self.assertEqual(result.sortit2(list2), [
                         1, 1, 1, 1, 1, 1, 3, 3, 5, 7, 8, 8, 8, 9])

    def test_sort0n1s(self):
        result = Methods()
        list1 = [0, 1, 1, 0, 0, 0, 1, 0, 1, 0]
        self.assertEqual(result.sort0n1s(list1), [
                         0, 0, 0, 0, 0, 0, 1, 1, 1, 1])


if __name__ == '__main__':
    unittest.main()
