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

    def test_with_alternate_words(self):
        with self.subTest(msg="Alternate Words: Divisible by None"):
            self.assertEqual(fizzbuzz_for_num(1, fizz_word="Ab", buzz_word="Cd"), "1")
        with self.subTest(msg="Alternate Words: Divisible by Three"):
            self.assertEqual(fizzbuzz_for_num(3, fizz_word="Ab", buzz_word="Cd"), "Ab")
        with self.subTest(msg="Alternate Words: Divisible by Five"):
            self.assertEqual(fizzbuzz_for_num(5, fizz_word="Ab", buzz_word="Cd"), "Cd")
        with self.subTest(msg="Alternate Words: Divisible by Both"):
            self.assertEqual(fizzbuzz_for_num(15, fizz_word="Ab", buzz_word="Cd"), "AbCd")

    def test_with_alternate_divisors(self):
        with self.subTest(msg="Alternate Divisors: Divisible by None"):
            self.assertEqual(fizzbuzz_for_num(1, fizz_divisor=7, buzz_divisor=11), "1")
        with self.subTest(msg="Alternate Divisors: Divisible by First"):
            self.assertEqual(fizzbuzz_for_num(7, fizz_divisor=7, buzz_divisor=11), "Fizz")
        with self.subTest(msg="Alternate Divisors: Divisible by Second"):
            self.assertEqual(fizzbuzz_for_num(11, fizz_divisor=7, buzz_divisor=11), "Buzz")
        with self.subTest(msg="Alternate Divisors: Divisible by Both"):
            self.assertEqual(fizzbuzz_for_num(77, fizz_divisor=7, buzz_divisor=11), "FizzBuzz")


if __name__ == "__main__":
    unittest.main(verbosity=2)
