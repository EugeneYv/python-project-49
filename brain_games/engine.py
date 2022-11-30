# общий модуль движок для всех игр
import prompt


def start_game(game):
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f'Hello, {name}!')
    print(game.RULE)
    i = 1
    while i < 4:
        result, question = game.get_game()  # было x.game()
        print(question)
        answer = prompt.string('Your answer: ')
        if answer != result:
            print(f"'{answer}' is wrong answer ;(."
                  f"Correct answer was '{result}'.")
            print(f'''Let's try again, {name}!''')
            return
        else:
            print("Correct!")
            i = i + 1
    print(f"Congratulations, {name}!")
    return
