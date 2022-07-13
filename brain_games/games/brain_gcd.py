import math
from random import randint


HELLO_MESSAGE = 'Find the greatest common divisor of given numbers.'


def get_question_with_answer():
    first_num = randint(1, 100)
    sec_num = randint(1, 100)
    correct_answer = math.gcd(first_num, sec_num)
    question = '{0} {1}'.format(first_num, sec_num)
    return question, str(correct_answer)
