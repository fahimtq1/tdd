from calc import SimpleCalc   # inheriting from the calculator script
import unittest
import pytest

class Calctest(unittest.TestCase):   # creating a class for unit testing

    calc_obj = SimpleCalc()   # creating an instance of the of SimpleCalc class

    def test_add(self):   # creating methods to test each part of the SimpleCalc program
        self.assertEqual(self.calc_obj.add(2, 4), 6)

    def test_subtract(self):
        self.assertEqual(self.calc_obj.subtract(4, 2), 2)

    def test_multiply(self):
        self.assertEqual(self.calc_obj.multiply(2, 2), 4)

    def test_divide(self):
        self.assertEqual(self.calc_obj.divide(4, 2), 2)

        self.assertRaises(ValueError, self.calc_obj.divide, 5, 0)   # there are different "assert" methods in unittest 

    def test_percentage(self):
        self.assertEqual(self.calc_obj.percentage(10, 100), 10)

    def test_cm_m(self):
        self.assertEqual(self.calc_obj.cm_m(1), 0.01)

    def test_year_of_birth(self):
        self.assertEqual(self.calc_obj.year_of_birth(22), 2000)
