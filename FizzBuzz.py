from InvalidNumberException import InvalidNumberException


class FizzBuzz:
    def __init__(self, number):
        self.number = number

    def play(self):
        if self.is_invalid():
            raise InvalidNumberException('Number is invalid.')
        if self.is_multiple_of_three_and_five():
            return "FizzBuzz"
        if self.is_multiple_of_three():
            return "Fizz"
        if self.is_multiple_of_five():
            return 'Buzz'
        else:
            return self.number

    def is_invalid(self):
        return self.number <= 0

    def is_multiple_of_three(self):
        return self.number % 3 == 0

    def is_multiple_of_five(self):
        return self.number % 5 == 0

    def is_multiple_of_three_and_five(self):
        return self.is_multiple_of_three() & self.is_multiple_of_five()






