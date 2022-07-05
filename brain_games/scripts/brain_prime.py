from brain_games.scripts.brain_games import base_game
from brain_games.games.brain_prime import brain_prime_question


def main():
    hello_string = 'Answer "yes" if given number is prime. '\
                   'Otherwise answer "no".'
    base_game(hello_string=hello_string,
              get_question_function=brain_prime_question)


if __name__ == '__main__':
    main()
