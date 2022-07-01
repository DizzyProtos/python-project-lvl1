from random import randint
from brain_games.scripts.brain_games import base_game


def brain_calc_question():
    fst_num = randint(1, 100)
    sec_num = randint(1, 100)

    math_symbols = ['+', '-', '*']
    operation_choice = randint(0, len(math_symbols))
    symb = math_symbols[operation_choice]
    correct_answer = eval('{0}{1}{2}'.format(fst_num, symb, sec_num))

    question_string = '{0} {1} {2}'.format(fst_num, symb, sec_num)
    return question_string, correct_answer


def main():
    hello_string = 'What is the result of the expression?'
    base_game(hello_string=hello_string,
              get_question_function=brain_calc_question)


if __name__ == '__main__':
    base_game()
