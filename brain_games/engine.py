from random import randint
import prompt


def welcome():
    print("Welcome to the Brain Games!")
    global name
#    name = ''
    name = prompt.string("May I have your name? ")
    print(f'Hello, {name}!')
    return name


def check_result(x):
    welcome()
    i = 1
    while 1 < 4:
        result, question = x.game()
        print(question)
        answer = prompt.string('Your answer: ')
        if answer != result:
            print(f''''{answer}' is wrong answer ;(. Correct answer was '{result}'.''')
            print(f'''Let's try again, {name}!''')
            break
        elif answer == result:
            print("Correct!")
        i = i + 1
        if i == 4:
            print(f"Congratulations, {name}!")
            break
