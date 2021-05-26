def checker():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name?')
    print('Hello, ', name)
    print('Answer "yes" if the number is even, otherwise answer "no".')
    i = 0
    while i <= 2:
        number = randint(1, 100)
        print('Question: ', number)
        answer = prompt.string('Your answer:')
        if i == 2:
            print(f'Congratulations, {name}!')
            break
        elif number % 2 == 0 and answer == 'yes':
            i += 1
            print(answer)
            print('Correct!')
        elif number % 2 == 1 and answer == 'no':
            i += 1
            print('Correct')
        elif answer != 'yes' or answer != 'no':
            print(f'\'yes\' is wrong answer ;(. Correct answer was \'no\'. Let\'s try again, {name}!')
            break