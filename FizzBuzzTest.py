import unittest
from InvalidNumberException import InvalidNumberException
from FizzBuzz import FizzBuzz


class FizzBuzzTest(unittest.TestCase):

    # Test si l'exception est bien retourné quand le nombre donnée est négatif.
    def test_if_number_is_negative(self):
        with self.assertRaises(InvalidNumberException):
            FizzBuzz(-2).play()

    # Test si l'exception est bien retourné quand le nombre donnée est zero.
    def test_if_number_is_equal_to_zero(self):
        with self.assertRaises(InvalidNumberException):
            FizzBuzz(0).play()

    # Test si Fizz est bien retourné quand le nombre donnée est un multiple de 3.
    def test_if_number_is_multiple_of_three(self):
        fizz = FizzBuzz(6)
        self.assertEqual("Fizz",fizz.play())

    # Test si Buzz est bien retourné quand le nombre donnée est un multiple de 5.
    def test_if_number_is_multiple_of_five(self):
        fizz = FizzBuzz(25)
        self.assertEqual("Buzz",fizz.play())

    # Test si FizzBuzz est bien retourné quand le nombre donnée est un multiple de 3 et 5.
    def test_if_number_is_multiple_of_three_and_five(self):
        fizz = FizzBuzz(15)
        self.assertEqual("FizzBuzz",fizz.play())

    # Test si le nombre donnée est bien retourné quand il ne rempli aucune des conditions précèdentes.
    def test_if_return_number(self):
        fizz = FizzBuzz(1)
        self.assertEqual(fizz.number,fizz.play())




