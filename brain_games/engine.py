import prompt
from brain_games import cli


def run_engine(game):
    QUANTITY_ROUND = 3
    start_round = 1
    print('Welcome to the Brain games!')
    name = cli.welcome_user()
    print(game.DESCRIPTION + '\n')
    while start_round <= QUANTITY_ROUND:
        result, question, = game.get_question_and_answer()
        print('Question: ' + question)
        answer = prompt.string('Your answer: ')
        if result == answer:
            print('Correct!')
            start_round += 1
        else:
            print(
                f'"{answer}" is wrong answer ;(. '
                f'Correct answer was "{result}". '
            )
            print(f'"Let\'s try again, {name}!"')
            return
    print(f'Congratulations, {name}!')
