"игра калькулятор"
from random import randint
from random import choice


RULE = 'What is the result of the expression?'
OPERATORS = ['-', '+', '*']


def get_game():
    random_number1 = randint(1, 10)
    random_number2 = randint(1, 10)
    operator = choice(OPERATORS)
    result = get_result(random_number1, random_number2, operator)
    question = str(f'Question: {random_number1} {operator} {random_number2}')
    return result, question


def get_result(first_number, second_number, operator):
    if operator == '-':
        result = str(first_number - second_number)
    if operator == '+':
        result = str(first_number + second_number)
    if operator == '*':
        result = str(first_number * second_number)
    return result
