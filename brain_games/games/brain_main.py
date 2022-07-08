import prompt


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))
    return name


def ask_for_answer(question_string, cor_answ, name):
    print(question_string)
    answer = prompt.string('Your answer: ')
    is_correct = answer == cor_answ
    if is_correct:
        print('Correct!')
    else:
        print(f"'{answer}' is wrong answer. Correct answer was {cor_answ}")
        print("Let's try again, {0}!".format(name))

    return is_correct


def base_game(game_module):
    name = welcome_user()
    print(game_module.hello_string)
    correct_count = 0
    points_to_win = 3
    while correct_count < points_to_win:
        base_question, correct_answer = game_module.get_question_function()
        question_string = 'Question: {0}'.format(base_question)
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
