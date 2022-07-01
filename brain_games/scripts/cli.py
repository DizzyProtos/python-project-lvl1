import prompt


def is_prime(n):
    for i in range(2, n):
        if (n % i) == 0:
            return False
    return True


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
