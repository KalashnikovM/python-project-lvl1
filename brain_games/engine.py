import prompt


def start(game):
    print('Start engineeeeeee!!!!!!!!!!')
    QUANTITY_ROUND = 3
    start_round = 1
    print('Welcome to the Brain games!')
    print(game.DESCRIPTION + '\n')
    name = prompt.string('May I have your name?')
    print(f'Hello, {name}')
    while start_round <= QUANTITY_ROUND:
        result, question, = game.get_question_and_answer()
        print('Question: ' + question)
        answer = prompt.string('Your answer: ')
        if result == answer:
            print('Correct!')
            start_round += 1
        else:
            print(f'"{answer}" is wrong answer ;(. Correct answer was "{result}".')
            print(f'"Let\'s try again, {name}!"')
            return
    print(f'Congratulations, {name}!')
