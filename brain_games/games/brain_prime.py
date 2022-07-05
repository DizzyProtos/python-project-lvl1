from random import randint
from brain_games.scripts.cli import is_prime


def brain_prime_question():
    random_num = randint(1, 100)
    correct_answer = 'yes' if is_prime(random_num) else 'no'
    question_string = '{0}'.format(random_num)
    return question_string, correct_answer
