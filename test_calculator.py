# https://github.com/fortune-emmanuel/Lab-11
# Partner 1: Fortune Emmanuel
# Partner 2: Daniel Ruiz
"""Unit tests for the Lab 11 calculator functions."""

import math
import unittest

import calculator


class TestCalculator(unittest.TestCase):
    # Partner 2 tests
    def test_add(self):
        self.assertEqual(calculator.add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(calculator.subtract(7, 4), 3)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            calculator.divide(0, 10)

    def test_logarithm(self):
        self.assertAlmostEqual(calculator.logarithm(2, 8), 3.0)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            calculator.logarithm(1, 10)
        with self.assertRaises(ValueError):
            calculator.logarithm(-2, 10)

    # Partner 1 tests
    def test_multiply(self):
        self.assertEqual(calculator.multiply(4, 5), 20)

    def test_divide(self):
        self.assertAlmostEqual(calculator.divide(2, 10), 5.0)

    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            calculator.logarithm(2, 0)
        with self.assertRaises(ValueError):
            calculator.logarithm(2, -8)

    def test_hypotenuse(self):
        self.assertAlmostEqual(calculator.hypotenuse(3, 4), 5.0)
        self.assertAlmostEqual(calculator.hypotenuse(-3, 4), 5.0)

    def test_sqrt(self):
        self.assertAlmostEqual(calculator.square_root(25), 5.0)
        with self.assertRaises(ValueError):
            calculator.square_root(-1)


if __name__ == "__main__":
    unittest.main()
