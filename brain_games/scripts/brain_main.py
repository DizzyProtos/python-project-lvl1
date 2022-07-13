import prompt
from brain_games.brain_main import run


def run_brain_game(game):
    run(game)


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))


if __name__ == '__main__':
    main()
