"игра на определение чётности числа"
from random import randint


RULE = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_game():
    random_number = randint(1, 20)
    if is_even(random_number):
        result = "yes"
    else:
        result = "no"
    question = str(f'Question: {random_number}')
    print(result)
    print(question)
    return result, question


def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False
