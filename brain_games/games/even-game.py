"игра на определение чётности числа"
from random import randint


GAME_ANNOUNCE = 'Answer "yes" if the number is even, otherwise answer "no".'


def game():
    random_digit = randint(1, 20)
    if random_digit % 2 == 0:
        result = "yes"
    else:
        result = "no"
    question = str(f'Question: {random_digit}')
    return result, question
