"игра калькулятор"
from random import randint
from random import choice


RULE = 'What is the result of the expression?'
OPERATORS = ['-', '+', '*']
make_choice = choice(OPERATORS)


def get_game():
    random_number1 = randint(1, 10)
    random_number2 = randint(1, 10)
    result = get_result(random_number1, random_number2)
    question = str(f'Question: {random_number1} {make_choice} {random_number2}')
    return result, question


def get_result(x, y):
    if make_choice == '-':
        result = str(x - y)
    if make_choice == '+':
        result = str(x + y)
    if make_choice == '*':
        result = str(x * y)
    return result
