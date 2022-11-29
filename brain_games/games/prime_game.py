"игра простое ли число"
from random import randint


GAME_ANNOUNCE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def game():
    random_digit = randint(2, 20)  # исходный вариант (1, 20)
    k = 0
    for i in range(2, random_digit // 2 + 1):
        if random_digit % i == 0:
            k = k + 1
    if k <= 0:
        result = "yes"
    else:
        result = "no"
    question = str(f'Question: {random_digit}')

    return result, question
