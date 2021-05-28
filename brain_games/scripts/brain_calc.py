#!/usr/bin/env python3
from random import randint, choice



def main():
    """Run an example code."""
    # it is ok to have some magical numbers locally
    calc()


def calc():
    num_operator = choice('-+*')
    f_num = randint(1, 99)
    s_num = randint(1, 99)
    if num_operator == '-':
        result = f_num - s_num
    elif num_operator == '+':
        result = f_num + s_num
    elif num_operator == '*'
        result = f_num * s_num
    question = f'{str(f_num)} {num_operator} {str(s_num)}
    return str(result), question




if __name__ == '__main__':
    main()
