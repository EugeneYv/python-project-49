# общий модуль движок для всех игр
import prompt


def start_game(game):
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f'Hello, {name}!')
    i = 1
    while 1 < 4:
        result, question = game.game()  # было x.game()
        print(question)
        answer = prompt.string('Your answer: ')
# result должен приходить в формате string
        if answer != result:
            print(f"'{answer}' is wrong answer ;(."      # f"''{answer}'
                  f"Correct answer was '{result}'.")
            print(f'''Let's try again, {name}!''')
            break
        elif answer == result:
            print("Correct!")
        i = i + 1
        if i == 4:
            print(f"Congratulations, {name}!")
            break
