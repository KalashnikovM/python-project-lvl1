import prompt


def welcome_user():
    name = prompt.string('May I hawe your name?')
    print('Hello, ', name)
