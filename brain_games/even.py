from random import randint
import prompt

def even():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    i = 1
    while i < 4:
        random_digit = randint(1, 20)
        if random_digit % 2 == 0:
            is_even = "yes"
        else:
            is_even = "no"
        print('''Answer "yes" if the number is even, otherwise answer "no".''')
        print(f'Question: {random_digit}')
        answer = prompt.string('Your answer: ')
        if answer != is_even:
            print(f''''{answer}' is wrong answer ;(. Correct answer was '{is_even}'.''')
            print(f'''Let's try again, {name}!''')
            break
        if answer == is_even:
            print("Correct!")
        i = i + 1
        if i == 4:
            print(f"Congratulations, {name}!")
