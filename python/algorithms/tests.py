import unittest
from bs import bs
from bubble_sort import bubble_sort
from selection_sort import selection_sort
from insertion_sort import insertion_sort
from merge_sort import merge_sort
from quick_sort import quick_sort
from r_quick_sort import r_quick_sort

class TestDataStructures(unittest.TestCase):

    def test_binary_search(self):
        test = [3, 3, 11, 12, 13, 21, 23, 23, 25, 27, 29, 32, 35, 51, 59, 68, 73, 77, 92]
        self.assertEqual(bs(test, 11), 2)
    def test_bubble_sort(self):
        test = [51, 3, 35, 92, 11, 13, 29, 12, 68, 77, 59, 25, 73, 32, 23, 3, 27, 23, 21]
        ans = [3, 3, 11, 12, 13, 21, 23, 23, 25, 27, 29, 32, 35, 51, 59, 68, 73, 77, 92]
        self.assertEqual(bubble_sort(test), ans)
    def test_selection_sort(self):
        test = [51, 3, 35, 92, 11, 13, 29, 12, 68, 77, 59, 25, 73, 32, 23, 3, 27, 23, 21]
        ans = [3, 3, 11, 12, 13, 21, 23, 23, 25, 27, 29, 32, 35, 51, 59, 68, 73, 77, 92]
        self.assertEqual(selection_sort(test), ans)
    def test_insertion_sort(self):
        test = [51, 3, 35, 92, 11, 13, 29, 12, 68, 77, 59, 25, 73, 32, 23, 3, 27, 23, 21]
        ans = [3, 3, 11, 12, 13, 21, 23, 23, 25, 27, 29, 32, 35, 51, 59, 68, 73, 77, 92]
        self.assertEqual(insertion_sort(test), ans)
    def test_merge_sort(self):
        test = [51, 3, 35, 92, 11, 13, 29, 12, 68, 77, 59, 25, 73, 32, 23, 3, 27, 23, 21]
        ans = [3, 3, 11, 12, 13, 21, 23, 23, 25, 27, 29, 32, 35, 51, 59, 68, 73, 77, 92]
        self.assertEqual(merge_sort(test), ans)
    def test_quick_sort(self):
        test = [51, 3, 35, 92, 11, 13, 29, 12, 68, 77, 59, 25, 73, 32, 23, 3, 27, 23, 21]
        ans = [3, 3, 11, 12, 13, 21, 23, 23, 25, 27, 29, 32, 35, 51, 59, 68, 73, 77, 92]
        self.assertEqual(quick_sort(test), ans)
    def test_random_quick_sort(self):
        test = [51, 3, 35, 92, 11, 13, 29, 12, 68, 77, 59, 25, 73, 32, 23, 3, 27, 23, 21]
        ans = [3, 3, 11, 12, 13, 21, 23, 23, 25, 27, 29, 32, 35, 51, 59, 68, 73, 77, 92]
        self.assertEqual(r_quick_sort(test), ans)


if __name__ == '__main__':
    unittest.main()

