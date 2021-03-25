import unittest


class FizzBuzzTest(unittest.TestCase):

    def test_if_number_is_negative(self):
        with self.assertRaises(InvalidNumberException):
            FizzBuzz(-2).play()

