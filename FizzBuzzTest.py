import unittest
from InvalidNumberException import InvalidNumberException
from FizzBuzz import FizzBuzz


class FizzBuzzTest(unittest.TestCase):

    def test_if_number_is_negative(self):
        with self.assertRaises(InvalidNumberException):
            FizzBuzz(-2).play()

    def test_if_number_is_equal_to_zero(self):
        with self.assertRaises(InvalidNumberException):
            FizzBuzz(0).play()



