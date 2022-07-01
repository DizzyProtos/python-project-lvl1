from random import randint
from brain_games.scripts.brain_games import base_game
from brain_games.scripts.cli import is_prime


def brain_prime_question():
    random_num = randint(1, 100)
    correct_answer = 'yes' if is_prime(random_num) else 'no'
    question_string = '{0}'.format(random_num)
    return question_string, correct_answer


def main():
    hello_string = 'Answer "yes" if given number is prime. '\
                   'Otherwise answer "no".'
    base_game(hello_string=hello_string,
              get_question_function=brain_prime_question)


if __name__ == '__main__':
    main()
