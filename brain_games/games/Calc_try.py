"игра калькулятор"
from random import randint


def game():
    random_digit1 = randint(1, 10)
    random_digit2 = randint(1, 10)
    random_digit3 = randint(1, 3)
    if random_digit3 == 1:
        sign = '+'
        result = str(random_digit1 + random_digit2)
    if random_digit3 == 2:
        sign = '-'
        result = str(random_digit1 - random_digit2)
    if random_digit3 == 3:
        sign = '*'
        result = str(random_digit1 * random_digit2)
    question_part1 = 'What is the result of the expression?\n'
    question_part2 = str(f'Question: {random_digit1} {sign} {random_digit2}')
    question = str(question_part1 + question_part2)
    return result, question
