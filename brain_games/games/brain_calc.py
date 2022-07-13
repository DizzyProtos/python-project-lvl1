from random import randint, choice


HELLO_MESSAGE = 'What is the result of the expression?'


def _calculate_answer(first_num, second_num, math_symbol):
    if math_symbol == '+':
        return first_num + second_num
    elif math_symbol == '-':
        return first_num - second_num
    elif math_symbol == '*':
        return first_num * second_num
    raise NotImplementedError(f'Math symbol {math_symbol} is not implemented')


def get_question_with_answer():
    fst_num = randint(1, 100)
    sec_num = randint(1, 100)

    math_symbols = ['+', '-', '*']
    symb = choice(math_symbols)
    correct_answer = _calculate_answer(fst_num, sec_num, symb)

    question = '{0} {1} {2}'.format(fst_num, symb, sec_num)
    return question, str(correct_answer)
