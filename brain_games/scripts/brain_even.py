import random
from brain_games.scripts.cli import welcome_user, ask_for_answer


def brain_even():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    correct_count = 0
    while correct_count < 3:
        some_number = int(random.random() * 100)
        question_string = 'Question: {0}'.format(some_number)
        correct_answer = 'yes' if some_number % 2 == 0 else 'no'

        is_correct = ask_for_answer(question_string, correct_answer, name)
        if is_correct:
            correct_count += 1
        else:
            return
    print('Congratulations, {0}!'.format(name))


def main():
    brain_even()


if __name__ == '__main__':
    brain_even()
