from random import randint


HELLO_MESSAGE = 'What number is missing in the progression?'


def get_question_with_answer():
    progression_length = 10

    random_diff = randint(1, 15)
    start_num = randint(0, 100)
    random_hide = randint(0, progression_length)

    progression = ''
    correct_answer = start_num + random_diff * random_hide
    for x in range(0, progression_length):
        new_num = start_num + random_diff * x
        progression += '{0} '.format(new_num)

    question = '{0}'.format(progression)
    question = question[:-1]
    question = question.replace(str(correct_answer), '..')
    return question, str(correct_answer)
