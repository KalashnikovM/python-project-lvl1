from random import randint, choice

DESCRIPTION = 'What number is missing in the progression?'


def get_question_and_answer():
    multiplier = randint(1, 25)
    check_position_num = randint(3, 20)
    my_seq = list(range(1, 300, multiplier))
    print('my_seq', my_seq)
    xx = my_seq[check_position_num]
    my_seq.insert(check_position_num, '. .')
    print('new my_seq', my_seq)
    print('multiplier', multiplier)
    print('Position ', check_position_num + 1)
    print(xx)


get_question_and_answer()
