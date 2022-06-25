import random
import math
from brain_games.scripts.cli import welcome_user, ask_for_answer


def brain_gcd():
    name = welcome_user()
    print('Find the greatest common divisor of given numbers.')
    correct_count = 0
    while correct_count < 3:
        first_num = int(random.random() * 100)
        sec_num = int(random.random() * 100)
        correct_answer = math.gcd(first_num, sec_num)
        question_string = 'Question: {0} {1}'.format(first_num, sec_num)

        is_correct = ask_for_answer(question_string, str(correct_answer), name)
        if is_correct:
            correct_count += 1
        else:
            return

    print('Congratulations, {0}!'.format(name))


def main():
    brain_gcd()


if __name__ == '__main__':
    brain_gcd()
