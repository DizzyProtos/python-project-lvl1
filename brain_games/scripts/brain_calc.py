from brain_games.scripts.brain_games import base_game
from brain_games.games.brain_calc import brain_calc_question


def main():
    hello_string = 'What is the result of the expression?'
    base_game(hello_string=hello_string,
              get_question_function=brain_calc_question)


if __name__ == '__main__':
    base_game()
