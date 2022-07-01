import math
from random import randint
from brain_games.scripts.brain_games import base_game


def brain_gcd_question():
    first_num = randint(1, 100)
    sec_num = randint(1, 100)
    correct_answer = math.gcd(first_num, sec_num)
    question_string = '{0} {1}'.format(first_num, sec_num)
    return question_string, correct_answer


def main():
    hello_string = 'Find the greatest common divisor of given numbers.'
    base_game(hello_string=hello_string,
              get_question_function=brain_gcd_question)


if __name__ == '__main__':
    main()
