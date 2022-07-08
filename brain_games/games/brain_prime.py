from random import randint


def _is_prime(n):
    if n <= 1:
        return False
    
    if n % 2 == 0:
        return False
    
    for i in range(3, int(n**0.5)+1, 2):
        if (n % i) == 0:
            return False
    return True


HELLO_MESSAGE = 'Answer "yes" if given number is prime. '\
                'Otherwise answer "no".'


def get_question_with_answer():
    random_num = randint(2, 100)
    correct_answer = 'yes' if _is_prime(random_num) else 'no'
    question = '{0}'.format(random_num)
    return question, correct_answer
