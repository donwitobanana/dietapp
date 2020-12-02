from random import randint, choice

class UpcGenerator:
    allowed_num_systems_a = [0, 1, 6, 7, 8, 9]
    allowed_num_systems_e = [0, 1]
    upc_e_patterns = [
        'XX00000XXX',
        'XX10000XXX',
        'XX20000XXX',
        'XXX00000XX',
        'XXXX00000X',
        'XXXXX00005',
        'XXXXX00006',
        'XXXXX00007',
        'XXXXX00008',
        'XXXXX00009',
    ]

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
    def _first_digit(cls, num_system):
        return choice(num_system)

    @classmethod
    def generate(cls):
        output = str(cls._first_digit(cls.allowed_num_systems_a))
        for _ in range(10):
            digit = randint(0, 9)
            output += str(digit)
        output += str(cls._last_digit(output))
        return output

    @classmethod
    def generate_from_pattern(cls):
        pattern = choice(cls.upc_e_patterns)
        output = str(cls._first_digit(cls.allowed_num_systems_e))
        for letter in pattern:
            if letter == 'X':
                output += str(randint(0, 9))
            else:
                output += letter
        output += str(cls._last_digit(output))
        return output
