"игра калькулятор"
from random import randint
from random import choice


GAME_ANNOUNCE = 'What is the result of the expression?'


def game():
    result = 'noresult'
    random_number1 = randint(1, 10)
    random_number2 = randint(1, 10)
    operators = ['-', '+', '*']
#    print(operators)
    make_choice = choice(operators)
#    print(make_choice)
    if make_choice == '-':
        result = str(random_number1 - random_number2)
#        print(result)
    if make_choice == '+':
        result = str(random_number1 + random_number2)
#        print(result)
    if make_choice == '*':
        result = str(random_number1 * random_number2)
#        print(result)
    question = str(f'Question: {random_number1} {make_choice} {random_number2}')
#    print(result)
#    print(question)
    return result, question


game()
