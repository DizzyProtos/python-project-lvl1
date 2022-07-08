from random import randint


def is_prime(n):
    for i in range(2, n):
        if (n % i) == 0:
            return False
    return True


hello_string = 'Answer "yes" if given number is prime. '\
               'Otherwise answer "no".'


def get_question_function():
    random_num = randint(1, 100)
    correct_answer = 'yes' if is_prime(random_num) else 'no'
    question_string = '{0}'.format(random_num)
    return question_string, correct_answer
