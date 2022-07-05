from brain_games.scripts.brain_games import base_game
from brain_games.games.brain_gcd import brain_gcd_question


def main():
    hello_string = 'Find the greatest common divisor of given numbers.'
    base_game(hello_string=hello_string,
              get_question_function=brain_gcd_question)


if __name__ == '__main__':
    main()
