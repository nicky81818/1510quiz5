from unittest import TestCase
from is_sorted import is_sorted


class Test(TestCase):
    def test_is_sorted_positive_sorted_list(self):
        expected_value = True
        actual_value = is_sorted([1, 2, 3])
        message = "positive sorted list test failure"
        self.assertEqual(expected_value, actual_value, message)

    def test_is_sorted_positive_unsorted_list(self):
        expected_value = False
        actual_value = is_sorted([3, 2, 1])
        message = "positive unsorted list test failure"
        self.assertEqual(expected_value, actual_value, message)

    def test_is_sorted_one_element_list(self):
        expected_value = True
        actual_value = is_sorted([1])
        message = "negative sorted list test failure"
        self.assertEqual(expected_value, actual_value, message)

    def test_is_sorted_many_element_list(self):
        expected_value = False
        actual_value = is_sorted([-1, -2, -3, 5, -10, 100])
        message = "negative unsorted list test failure"
        self.assertEqual(expected_value, actual_value, message)

    def test_is_sorted_empty_list(self):
        expected_value = True
        actual_value = is_sorted([])
        message = "empty list test failure"
        self.assertEqual(expected_value, actual_value, message)
