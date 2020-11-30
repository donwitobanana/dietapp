from random import randint, choice

class UpcGenerator:
    allowed_num_systems = [0, 1, 6, 7, 8, 9]

    @classmethod
    def _last_digit(cls, code):
        digits = [int(digit) for digit in code]
        odd_sum = sum(digits[::2])
        even_sum = sum(digits[1::2])
        result = (odd_sum * 3 + even_sum) % 10
        if result != 0:
            result = 10 - result
        return result

    @classmethod
    def _first_digit(cls):
        return choice(cls.allowed_num_systems)

    @classmethod
    def generate(cls):
        output = str(cls._first_digit())
        for _ in range(10):
            digit = randint(0, 9)
            output += str(digit)
        output += str(cls._last_digit(output))
        return output
