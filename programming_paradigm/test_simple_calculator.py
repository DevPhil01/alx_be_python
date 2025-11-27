# test_simple_calculator.py

import unittest
from simple_calculator import SimpleCalculator


class TestSimpleCalculator(unittest.TestCase):
    """
    Comprehensive unit tests for the SimpleCalculator class.
    """

    def setUp(self):
        """
        Create a fresh SimpleCalculator instance before each test method.
        This ensures test isolation.
        """
        self.calc = SimpleCalculator()

    # ========================
    # Tests for add() method
    # ========================
    def test_addition_positive_numbers(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(10, 20), 30)

    def test_addition_negative_numbers(self):
        self.assertEqual(self.calc.add(-5, -7), -12)
        self.assertEqual(self.calc.add(-10, 8), -2)

    def test_addition_mixed_signs(self):
        self.assertEqual(self.calc.add(-5, 10), 5)
        self.assertEqual(self.calc.add(7, -3), 4)

    def test_addition_with_zero(self):
        self.assertEqual(self.calc.add(0, 5), 5)
        self.assertEqual(self.calc.add(5, 0), 5)
        self.assertEqual(self.calc.add(0, 0), 0)

    def test_addition_floats(self):
        self.assertEqual(self.calc.add(1.5, 2.5), 4.0)
        self.assertAlmostEqual(self.calc.add(0.1, 0.2), 0.3)  # Floating-point safety

    # ===========================
    # Tests for subtract() method
    # ===========================
    def test_subtraction_positive(self):
        self.assertEqual(self.calc.subtract(10, 5), 5)
        self.assertEqual(self.calc.subtract(20, 10), 10)

    def test_subtraction_negative_result(self):
        self.assertEqual(self.calc.subtract(5, 10), -5)

    def test_subtraction_with_zero(self):
        self.assertEqual(self.calc.subtract(10, 0), 10)
        self.assertEqual(self.calc.subtract(0, 5), -5)

    def test_subtraction_floats(self):
        self.assertEqual(self.calc.subtract(5.5, 2.3), 3.2)
        self.assertAlmostEqual(self.calc.subtract(0.1, 0.1), 0.0)

    # ===========================
    # Tests for multiply() method
    # ===========================
    def test_multiplication_positive(self):
        self.assertEqual(self.calc.multiply(3, 4), 12)
        self.assertEqual(self.calc.multiply(5, 5), 25)

    def test_multiplication_by_zero(self):
        self.assertEqual(self.calc.multiply(10, 0), 0)
        self.assertEqual(self.calc.multiply(0, 100), 0)
        self.assertEqual(self.calc.multiply(0, 0), 0)

    def test_multiplication_negatives(self):
        self.assertEqual(self.calc.multiply(-3, 5), -15)
        self.assertEqual(self.calc.multiply(4, -6), -24)
        self.assertEqual(self.calc.multiply(-3, -4), 12)

    def test_multiplication_floats(self):
        self.assertEqual(self.calc.multiply(2.5, 2), 5.0)
        self.assertAlmostEqual(self.calc.multiply(0.1, 0.2), 0.02)

    # =========================
    # Tests for divide() method
    # =========================
    def test_division_normal(self):
        self.assertEqual(self.calc.divide(10, 2), 5.0)
        self.assertEqual(self.calc.divide(15, 3), 5.0)
        self.assertEqual(self.calc.divide(7, 2), 3.5)

    def test_division_by_zero_returns_none(self):
        self.assertIsNone(self.calc.divide(10, 0))
        self.assertIsNone(self.calc.divide(-5, 0))
        self.assertIsNone(self.calc.divide(0, 0))

    def test_division_zero_by_nonzero(self):
        self.assertEqual(self.calc.divide(0, 5), 0.0)
        self.assertEqual(self.calc.divide(0, -3), -0.0)  # Special case in Python

    def test_division_negative_numbers(self):
        self.assertEqual(self.calc.divide(10, -2), -5.0)
        self.assertEqual(self.calc.divide(-15, 5), -3.0)
        self.assertEqual(self.calc.divide(-8, -4), 2.0)

    def test_division_floats(self):
        self.assertAlmostEqual(self.calc.divide(1, 3), 0.3333333333333333)
        self.assertEqual(self.calc.divide(5.0, 2.0), 2.5)


# Run the tests when script is executed directly
if __name__ == "__main__":
    unittest.main(verbosity=2)
