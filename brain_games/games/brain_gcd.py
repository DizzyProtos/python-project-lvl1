import math
from random import randint


hello_string = 'Find the greatest common divisor of given numbers.'


def brain_gcd_question():
    first_num = randint(1, 100)
    sec_num = randint(1, 100)
    correct_answer = math.gcd(first_num, sec_num)
    question_string = '{0} {1}'.format(first_num, sec_num)
    return question_string, correct_answer
