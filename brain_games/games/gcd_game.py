"игра на нахождение НОД"
from math import gcd
from random import randint


GAME_ANNOUNCE = 'Find the greatest common divisor of given numbers.'

def game():
    random_digit1 = randint(1, 100)
    random_digit2 = randint(1, 100)
    result = str(gcd(random_digit1, random_digit2))
    question = str(f'Question: {random_digit1} {random_digit2}')
    return result, question
