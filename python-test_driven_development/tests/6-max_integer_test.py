#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Define unittests for max_integer([..]).
    """

    def test_max_integer(self):
        self.assertEqual(max_integer([1, 2, 3, 5, 4]), 5)

    def test_max_integer_at_end(self):
        self.assertEqual(max_integer([1, 2, 3, 5, 4, 7]), 7)

    def test_max_integer_negation(self):
        self.assertEqual(max_integer([-1, -2, -3, -5, -4]), -1)

    def test_max_integer_with_negation(self):
        self.assertEqual(max_integer([-1, 0, -3, 5, 1]), 5)

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_zero(self):
        self.assertEqual(max_integer([0, 0]), 0)

    def test_one_number(self):
        self.assertEqual(max_integer([1]), 1)

    def test_same_number(self):
        self.assertEqual(max_integer([1, 1, 1]), 1)

    def test_big_list(self):
        self.assertEqual(max_integer([
            1, 2, 9, 8, 7, 5, 12, 50, 80,
            45, 4, 65, 75, 98, 1500, 200,
            744, 655, 122, 75, 88, 63, 32,
            887, 664, 123, 124, 125, 126]), 1500)

    def test_error_is_string(self):
        with self.assertRaises(TypeError):
            max_integer([0, "1"])

    def test_error_is_list_list(self):
        with self.assertRaises(TypeError):
            max_integer([0, [10, 20]])

    def test_error_is_tuple(self):
        with self.assertRaises(TypeError):
            max_integer([0, (1, 2)])

    def test_error_is_number(self):
        with self.assertRaises(TypeError):
            max_integer(5)

    def test_error_is_dictionary(self):
        with self.assertRaises(KeyError):
            max_integer({'key1': 1, 'key2': 2})
