from random import randint


def brain_even_question():
    some_number = randint(1, 100)
    question_string = '{0}'.format(some_number)
    correct_answer = 'yes' if some_number % 2 == 0 else 'no'
    return question_string, correct_answer
