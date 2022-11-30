"игра на нахождение НОД"
from math import gcd
from random import randint


RULE = 'Find the greatest common divisor of given numbers.'


def get_game():
    random_digit1 = randint(1, 100)
    random_digit2 = randint(1, 100)
    result = str(gcd(random_digit1, random_digit2))
    question = str(f'Question: {random_digit1} {random_digit2}')
    return result, question
