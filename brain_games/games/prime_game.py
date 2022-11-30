"игра простое ли число"
from random import randint


RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_game():
    random_number = randint(2, 20)
    if is_prime(random_number):
        result = 'yes'
    else:
        result = 'no'
    question = str(f'Question: {random_number}')
    return result, question


def is_prime(x):
    k = 0
    for i in range(2, x // 2 + 1):
        if x % i == 0:
            k = k + 1
    if k <= 0:
        return True
    else:
        return False
