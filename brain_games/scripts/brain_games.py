from brain_games.scripts.cli import ask_for_answer
from brain_games.scripts.cli import welcome_user


def base_game(hello_string, get_question_function):
    name = welcome_user()
    print(hello_string)
    correct_count = 0
    points_to_win = 3
    while correct_count < points_to_win:
        base_question, correct_answer = get_question_function()
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
