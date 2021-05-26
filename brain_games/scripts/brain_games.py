#!/usr/bin/env python
from brain_games.cli import welcome_user
from brain_even import checker


def main():
    """Run an example code."""
    # it is ok to have some magical numbers locally
    print('Welcome to the Brain Games!')
    welcome_user()
    checker()


if __name__ == '__main__':
    main()
