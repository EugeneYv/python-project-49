"игра простое ли число"
from random import randint


def game():
    random_digit = randint(1, 20)
    k = 0
    for i in range(2, random_digit // 2 + 1):
        if random_digit % i == 0:
            k = k + 1
    if k <= 0:
        result = "yes"
    else:
        result = "no"
    question_part1 = '''Answer "yes" if given number is prime. Otherwise answer "no".\n'''
    question_part2 = str(f'Question: {random_digit}')
    question = str(question_part1 + question_part2)
    return result, question
