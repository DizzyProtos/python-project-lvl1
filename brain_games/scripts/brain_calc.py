import random
from brain_games.scripts.cli import welcome_user, ask_for_answer


def brain_calc():
    name = welcome_user()
    print('What is the result of the expression?')
    correct_count = 0
    while correct_count < 3:
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

        is_correct = ask_for_answer(question_string, str(correct_answer), name)
        if is_correct:
            correct_count += 1
        else:
            return

    print('Congratulations, {0}!'.format(name))


def main():
    brain_calc()


if __name__ == '__main__':
    brain_calc()
