import random
import math
from brain_games.scripts.cli import ask_for_answer
from brain_games.scripts.cli import welcome_user
from brain_games.scripts.cli import get_random_number
from brain_games.scripts.cli import is_prime


brain_even_name = 'brain-even'
brain_prime_name = 'brain-prime'
brain_gcd_name = 'brain-gcd'
brain_progression_name = 'brain-progression'
brain_calc_name = 'brain-calc'


def get_hello_string(game_type):
    if game_type == brain_even_name:
        return 'Answer "yes" if the number is even, otherwise answer "no".'
    elif game_type == brain_prime_name:
        return 'Answer "yes" if given number is prime. Otherwise answer "no".'
    elif game_type == brain_gcd_name:
        return 'Find the greatest common divisor of given numbers.'
    elif game_type == brain_progression_name:
        return 'What number is missing in the progression?'
    elif game_type == brain_calc_name:
        return 'What is the result of the expression?'


def brain_even_question():
    some_number = int(random.random() * 100)
    question_string = 'Question: {0}'.format(some_number)
    correct_answer = 'yes' if some_number % 2 == 0 else 'no'
    return question_string, correct_answer


def brain_prime_question():
    random_num = int(random.random() * 100)
    correct_answer = 'yes' if is_prime(random_num) else 'no'
    question_string = 'Question: {0}'.format(random_num)
    return question_string, correct_answer


def brain_progression_question():
    random_diff = get_random_number(1, 15)
    start_num = get_random_number(0, 100)
    random_hide = get_random_number(0, 10)

    progression = ''
    correct_answer = 0
    for x in range(0, 10):
        new_num = start_num + random_diff * x
        if x == random_hide:
            correct_answer = str(new_num)
        progression += '{0} '.format(new_num)

    question_string = 'Question: {0}'.format(progression)
    question_string = question_string[:-1]
    question_string = question_string.replace(str(correct_answer), '..')
    return question_string, correct_answer


def brain_gcd_question():
    first_num = int(random.random() * 100)
    sec_num = int(random.random() * 100)
    correct_answer = math.gcd(first_num, sec_num)
    question_string = 'Question: {0} {1}'.format(first_num, sec_num)
    return question_string, correct_answer


def brain_calc_question():
    fst_num = int(random.random() * 100)
    sec_num = int(random.random() * 100)
    operation_choice = random.random()
    if operation_choice < 0.3:
        symb = '+'
        correct_answer = fst_num + sec_num
    elif operation_choice < 0.6:
        symb = '-'
        correct_answer = fst_num - sec_num
    else:
        symb = '*'
        correct_answer = fst_num * sec_num
    question_string = 'Question: {0} {1} {2}'.format(fst_num, symb, sec_num)
    return question_string, correct_answer


def get_question(game_type):
    if game_type == brain_even_name:
        return brain_even_question()
    elif game_type == brain_prime_name:
        return brain_prime_question()
    elif game_type == brain_gcd_name:
        return brain_gcd_question()
    elif game_type == brain_progression_name:
        return brain_progression_question()
    elif game_type == brain_calc_name:
        return brain_calc_question()


def base_game(game_type):
    name = welcome_user()
    hello_string = get_hello_string(game_type)
    print(hello_string)
    correct_count = 0
    while correct_count < 3:
        question_string, correct_answer = get_question(game_type)
        correct_answer = str(correct_answer)
        is_correct = ask_for_answer(question_string, correct_answer, name)
        if is_correct:
            correct_count += 1
        else:
            return
    print('Congratulations, {0}!'.format(name))


def main():
    welcome_user()


if __name__ == '__main__':
    welcome_user()
