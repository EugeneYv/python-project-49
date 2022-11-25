"игра на определение чётности числа"
from random import randint


def game():
    random_digit = randint(1, 20)
    if random_digit % 2 == 0:
        result = "yes"
    else:
        result = "no"
    question_part1 = '''Answer "yes" if the number is even, otherwise answer "no".\n'''
    question_part2 = str(f'Question: {random_digit}')
    question = str(question_part1 + question_part2)
    return result, question
