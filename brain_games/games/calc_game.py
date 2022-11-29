"игра калькулятор"
from random import randint
from random import choice


GAME_ANNOUNCE = 'What is the result of the expression?'


def game():
    random_number1 = randint(1, 10)
    random_number2 = randint(1, 10)
    operators = ['-', '+', '*']
    make_choice = choice(operators)
    question = str(f'Question: {random_number1} {make_choice} {random_number2}')
    return result, question
