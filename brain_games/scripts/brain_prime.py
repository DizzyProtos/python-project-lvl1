import random
from brain_games.scripts.cli import welcome_user, ask_for_answer


def is_prime(n):
    for i in range(2, n):
        if (n % i) == 0:
            return False
    return True


def brain_prime():
    name = welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    correct_count = 0
    while correct_count < 3:
        random_num = int(random.random() * 100)
        correct_answer = 'yes' if is_prime(random_num) else 'no'
        question_string = 'Question: {0}'.format(random_num)

        is_correct = ask_for_answer(question_string, str(correct_answer), name)
        if is_correct:
            correct_count += 1
        else:
            correct_count = 0

    print('Congratulations, {0}!'.format(name))


def main():
    brain_prime()


if __name__ == '__main__':
    brain_prime()
