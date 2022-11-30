"игра прогрессия"
from random import randint

RULE = 'What number is missing in the progression?'


def get_game():
    random_index = randint(1, 10)
    number_list = get_progression()
    result = str(number_list[random_index])
    number_list[random_index] = '..'
    string_list = [str(i) for i in number_list]
    string = (" ".join(string_list))
    question = str(f'Question: {string}')
    print(result)
    return result, question


def get_progression():
    step = randint(1, 10)  # выставляем шаг между числами
    start_number = randint(1, 10)  # начальное число
    list = [start_number]
    for i in range(1, 11):
        append_number = start_number + step
        list.append(append_number)
        start_number = append_number
    return list
