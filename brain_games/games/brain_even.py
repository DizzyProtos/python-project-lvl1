from random import randint


hello_string = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_question_function():
    some_number = randint(1, 100)
    question_string = '{0}'.format(some_number)
    correct_answer = 'yes' if some_number % 2 == 0 else 'no'
    return question_string, correct_answer
