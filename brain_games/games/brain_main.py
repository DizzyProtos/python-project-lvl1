import prompt


def base_game(game_module):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))

    print(game_module.hello_string)
    correct_count = 0
    points_to_win = 3
    while correct_count < points_to_win:
        base_question, correct_answer = game_module.get_question_function()
        question_string = 'Question: {0}'.format(base_question)
        correct_answer = str(correct_answer)

        print(question_string)
        answer = prompt.string('Your answer: ')
        is_correct = answer == correct_answer
        if is_correct:
            print('Correct!')
            correct_count += 1
        else:
            print(f"'{answer}' is wrong answer" \
                  f"Correct answer was {correct_answer}")
            print("Let's try again, {0}!".format(name))
            return
    print('Congratulations, {0}!'.format(name))
