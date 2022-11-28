"игра простое ли число"
from random import randint


def game():
    random_digit = randint(2, 20) # исходный вариант (1, 20)
    k = 0
    for i in range(2, random_digit // 2 + 1):
        if random_digit % i == 0:
            k = k + 1
    if k <= 0:
        result = "yes"
    else:
        result = "no"
    question_part1 = '''Answer "yes" if given number is prime.'''
    question_part2 = ''' Otherwise answer "no".\n'''
    question_part3 = str(f'Question: {random_digit}')
    question = str(question_part1 + question_part2 + question_part3)
    return result, question
