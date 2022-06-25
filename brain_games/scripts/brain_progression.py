import random
# from brain_games.scripts.cli import welcome_user, ask_for_answer


def brain_progression():
    # name = welcome_user()
    print('What number is missing in the progression?')
    correct_count = 0
    while correct_count < 3:
        random_diff = int(random.random() * 15)
        start_num = int(random.random() * 100)
        random_hide = int(random.random() * 10)

        progression = ''
        correct_answer = 0
        for x in range(0, 10):
            new_num = start_num + random_diff * x
            if x == random_hide:
                correct_answer = str(new_num)
            progression += '{0}, '.format(new_num)

        question_string = 'Question: {0}'.format(progression)
        question_string = question_string.replace(', {0},'.format(correct_answer), ' ..')

        is_correct = ask_for_answer(question_string, str(correct_answer), name)
        if is_correct:
            correct_count += 1
        else:
            return

    print('Congratulations, {0}!'.format(name))


def main():
    brain_progression()


if __name__ == '__main__':
    brain_progression()
