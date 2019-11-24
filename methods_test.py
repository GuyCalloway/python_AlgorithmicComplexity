import unittest
from methods import Methods


class TestMethods(unittest.TestCase):

    def test_if_method_reverses_string(self):
        result = Methods
        list1 = [5, 1, 2, 3, 1, 4, 5, 5, 6, 4, 7]
        self.assertEqual(result.reverse(self, list1), [
                         7, 4, 6, 5, 5, 4, 1, 3, 2, 1, 5])

    def test_if_counts_number_of_duplicatesDOUBLESONLY(self):
        result = Methods
        list1 = [5, 1, 2, 3, 1, 4, 5, 5, 6, 4, 7]
        self.assertEqual(result.find_duplicates(self, list1), [1, 4])

    def test_if_shuffles_list(self):
        result = Methods
        list1 = [5, 1, 2, 3, 1, 4, 5, 5, 6, 4, 7]
        self.assertNotEqual(result.shuffle(self, list1), list1)
        self.assertEqual(len(result.shuffle(self, list1)), len(list1))

    def test_find_most_feq_val(self):
        result = Methods
        list1 = [5, 1, 2, 3, 3, 3, 1, 4, 5, 5, 6, 4, 4, 7]
        self.assertEqual(result.find_most_freq_values(self, list1), [5, 3, 4])


if __name__ == '__main__':
    unittest.main()
