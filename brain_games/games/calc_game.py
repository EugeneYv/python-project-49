"игра калькулятор"
from random import randint
from random import choice


RULE = 'What is the result of the expression?'
OPERATORS = ['-', '+', '*']


def get_game():
    random_number1 = randint(1, 10)
    random_number2 = randint(1, 10)
    global make_choice
    make_choice = choice(OPERATORS)
    result = get_result(random_number1, random_number2)
    question = str(f'Question: {random_number1} {make_choice} {random_number2}')
    print(result)
    print(question)
    return result, question


def get_result(x, y):
    if make_choice == '-':
        result = str(x - y)
    if make_choice == '+':
        result = str(x + y)
    if make_choice == '*':
        result = str(x * y)
    return result
