from InvalidNumberException import InvalidNumberException


class FizzBuzz:
    def __init__(self, number):
        self.number = number

    def play(self):
        multiple_of_three = self.number % 3 == 0
        multiple_of_five = self.number % 5 == 0

        if self.number <= 0:
            raise InvalidNumberException('Number is invalid.')
        if multiple_of_three and multiple_of_five:
            return "FizzBuzz"
        if multiple_of_three:
            return "Fizz"
        if multiple_of_five:
            return 'Buzz'
        else:
            return self.number





