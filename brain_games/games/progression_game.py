"игра прогрессия"
from random import randint

GAME_ANNOUNCE = 'What number is missing in the progression?'


def game():
    random_index = randint(1, 10)
    number_list = progression()
    result = str(number_list[random_index])
    number_list[random_index] = '..'
    string = str(number_list).strip('[]').replace("'", "").replace(",", "")
    question = str(f'Question: {string}')
    return result, question


def progression():
    step = randint(1, 10)  # выставляем шаг между числами
    start_number = randint(1, 10)  # начальное число
    list = [start_number]
    for i in range(1, 11):
        append_number = start_number + step
        list.append(append_number)
        start_number = append_number
    return list
