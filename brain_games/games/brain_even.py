from random import randint


HELLO_MESSAGE = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_question_with_answer():
    some_number = randint(1, 100)
    question = '{0}'.format(some_number)
    correct_answer = 'yes' if some_number % 2 == 0 else 'no'
    return question, correct_answer
