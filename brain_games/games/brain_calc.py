from random import randint


def brain_calc_question():
    fst_num = randint(1, 100)
    sec_num = randint(1, 100)

    math_symbols = ['+', '-', '*']
    operation_choice = randint(0, len(math_symbols) - 1)
    symb = math_symbols[operation_choice]
    correct_answer = eval('{0}{1}{2}'.format(fst_num, symb, sec_num))

    question_string = '{0} {1} {2}'.format(fst_num, symb, sec_num)
    return question_string, correct_answer
