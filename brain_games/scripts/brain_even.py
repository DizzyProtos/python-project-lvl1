from random import randint
from brain_games.scripts.brain_games import base_game


def brain_even_question():
    some_number = randint(1, 100)
    question_string = '{0}'.format(some_number)
    correct_answer = 'yes' if some_number % 2 == 0 else 'no'
    return question_string, correct_answer


def main():
    hello_string = 'Answer "yes" if the number is even, otherwise answer "no".'
    base_game(hello_string=hello_string,
              get_question_function=brain_even_question)


if __name__ == '__main__':
    main()
