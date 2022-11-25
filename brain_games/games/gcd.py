"игра на нахождение НОД"
from math import gcd
from random import randint


def game():
    random_digit1 = randint(1, 100)
    random_digit2 = randint(1, 100)
    result = str(gcd(random_digit1, random_digit2))
    question_part1 = 'Find the greatest common divisor of given numbers.\n'
    question_part2 = str(f'Question: {random_digit1} {random_digit2}')
    question = str(question_part1 + question_part2)
    return result, question
