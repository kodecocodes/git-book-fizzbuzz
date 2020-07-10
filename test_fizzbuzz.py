#!/usr/bin/env python

import sys
sys.dont_write_bytecode = True  # Don't write *.pyc files

import unittest
from fizzbuzz import fizzbuzz_for_num


class TestFizzBuzz(unittest.TestCase):
    def test_divisible_by_none(self):
        self.assertEqual(fizzbuzz_for_num(1), "1")
        self.assertEqual(fizzbuzz_for_num(2), "2")

    def test_divisible_by_three(self):
        self.assertEqual(fizzbuzz_for_num(6), "Fizz")
        self.assertEqual(fizzbuzz_for_num(9), "Fizz")

    def test_divisible_by_five(self):
        self.assertEqual(fizzbuzz_for_num(10), "Buzz")
        self.assertEqual(fizzbuzz_for_num(20), "Buzz")

    def test_divisible_by_both(self):
        self.assertEqual(fizzbuzz_for_num(15), "FizzBuzz")
        self.assertEqual(fizzbuzz_for_num(30), "FizzBuzz")


if __name__ == "__main__":
    unittest.main(verbosity=2)
