#!/usr/bin/env python
# -*- coding: utf-8 -*-

from fizzbuzz import fizzbuzz
import unittest


class FizzBuzzTestCase:
    def __init__(self, value, expected):
        self.value = value
        self.expected = expected


class TestFizzBuzz(unittest.TestCase):
    """ test class of fizzbuzz.py
    """

    def test_fizzbuzz_one(self):
        # Arrange
        cases = [
            FizzBuzzTestCase(1, "1"),
            FizzBuzzTestCase(3, "fizz"),
            FizzBuzzTestCase(5, "buzz"),
            FizzBuzzTestCase(15, "fizzbuzz")]

        for case in cases:
            # Act
            actual = fizzbuzz(case.value)

            # Assert
            self.assertEqual(case.expected, actual)
