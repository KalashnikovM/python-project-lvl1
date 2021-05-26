from random import randint
import prompt


def main():
    """Run an example code."""
    # it is ok to have some magical numbers locally
    checker()


if __name__ == '__main__':
    main()


def checker():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello,  {name}')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    i = 0
    while i <= 2:
        number = randint(1, 100)
        print('Question: ', number)
        answer = prompt.string('Your answer:')
        check = check_digit(number, answer)
        if i == 2:
            print(f'Congratulations, {name}!')
            break
        elif check:
            i += 1
            print(f'{answer} \nCorrect')
        elif not check:
            print(f'\'yes\' is wrong answer ;(. Correct answer was \'no\'. Let\'s try again, {name}!')
            break


def check_digit(number, answer):
    if number % 2 == 1 and answer == 'no':
        return True
    elif number % 2 == 0 and answer == 'yes':
        return True
    else:
        return False
