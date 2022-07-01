from random import randint
from brain_games.scripts.brain_games import base_game


def brain_progression_question():
    progression_length = 10

    random_diff = randint(1, 15)
    start_num = randint(0, 100)
    random_hide = randint(0, progression_length)

    progression = ''
    correct_answer = 0
    for x in range(0, progression_length):
        new_num = start_num + random_diff * x
        if x == random_hide:
            correct_answer = str(new_num)
        progression += '{0} '.format(new_num)

    question_string = '{0}'.format(progression)
    question_string = question_string[:-1]
    question_string = question_string.replace(str(correct_answer), '..')
    return question_string, correct_answer


def main():
    hello_string = 'What number is missing in the progression?'
    base_game(hello_string=hello_string,
              get_question_function=brain_progression_question)


if __name__ == '__main__':
    main()
