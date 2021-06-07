import prompt


def welcome_user():
    name = prompt.string('May I hawe your name? ')
    welcome = f'Hello, {name}'
    print('\n' + welcome)
