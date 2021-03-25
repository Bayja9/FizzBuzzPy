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

    def test_if_number_is_multiple_of_three(self):
        fizz = FizzBuzz(6)
        self.assertEqual("Fizz",fizz.play())

    def test_if_number_is_multiple_of_five(self):
        fizz = FizzBuzz(25)
        self.assertEqual("Buzz",fizz.play())



