"игра прогрессия"
from random import randint


def game():
    step = randint(1, 10)  # выставляем шаг между числами
    digits_number = 10    # количество чисел
    start_digit = randint(1, 10)  # начальное число
    digit_list = [start_digit]
    for i in range(1, 11):
        new_digit = start_digit + step
        digit_list.extend([new_digit])
        start_digit = new_digit
    random_index = randint(1, 10)
    result = str(digit_list[random_index])
    digit_list[random_index] = '..'
    digit_string = str(digit_list).strip('[]').replace("'", "").replace(",", "")
    question_part1 = 'What number is missing in the progression?\n'
    question_part2 = str(f'Question: {digit_string}')
    question = str(question_part1 + question_part2)
    return result, question
