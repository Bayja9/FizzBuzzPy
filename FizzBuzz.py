from InvalidNumberException import InvalidNumberException


class FizzBuzz:
    def __init__(self, number):
        self.number = number

    def play(self):
        if self.number < 0:
            raise InvalidNumberException('Number is invalid.')
        if self.number == 0:
            raise InvalidNumberException("Number is invalid")
        if self.number % 3 == 0 and self.number % 5 == 0:
            return "FizzBuzz"
        if self.number % 3 == 0:
            return "Fizz"
        if self.number % 5 == 0:
            return 'Buzz'
        else:
            return self.number


