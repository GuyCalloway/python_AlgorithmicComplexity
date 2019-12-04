import unittest
from refined import RefinedMethods


class TestMethods(unittest.TestCase):

    def test_if_method_merges_two_sorted_arrays(self):
        result = RefinedMethods()
        list1 = [1, 1, 2, 5, 7, 10]
        list2 = [3, 4, 5, 5, 6, 11]
        self.assertEqual(result.merge_2_sorted_arrays(list1, list2), [
                         1, 1, 2, 3, 4, 5, 5, 5, 6, 7, 10, 11])
