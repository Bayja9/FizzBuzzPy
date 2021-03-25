from InvalidNumberException import InvalidNumberException


class FizzBuzz:
    def __init__(self, number):
        self.number = number

    def play(self):
        if self.number < 0:
            raise InvalidNumberException('Number is invalid.')
