from brain_games.scripts.brain_games import base_game
from brain_games.games.brain_even import brain_even_question


def main():
    hello_string = 'Answer "yes" if the number is even, otherwise answer "no".'
    base_game(hello_string=hello_string,
              get_question_function=brain_even_question)


if __name__ == '__main__':
    main()
