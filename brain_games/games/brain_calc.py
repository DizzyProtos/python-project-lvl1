from random import randint


HELLO_STRING = 'What is the result of the expression?'


def get_question_with_answer():
    fst_num = randint(1, 100)
    sec_num = randint(1, 100)

    math_symbols = ['+', '-', '*']
    operation_choice = randint(0, len(math_symbols) - 1)
    symb = math_symbols[operation_choice]
    correct_answer = eval('{0}{1}{2}'.format(fst_num, symb, sec_num))

    question = '{0} {1} {2}'.format(fst_num, symb, sec_num)
    return question, correct_answer
