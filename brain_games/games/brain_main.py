import prompt


def run_game(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))

    print(game.HELLO_MESSAGE)
    correct_count = 0
    points_to_win = 3
    while correct_count < points_to_win:
        base_question, correct_answer = game.get_question_with_answer()
        question = 'Question: {0}'.format(base_question)
        correct_answer = str(correct_answer)

        print(question)
        answer = prompt.string('Your answer: ')
        is_correct = answer == correct_answer
        if is_correct:
            print('Correct!')
            correct_count += 1
        else:
            print(f"'{answer}' is wrong answer"
                  f"Correct answer was {correct_answer}")
            print("Let's try again, {0}!".format(name))
            return
    print('Congratulations, {0}!'.format(name))
