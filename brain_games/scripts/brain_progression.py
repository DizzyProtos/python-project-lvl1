from brain_games.scripts.brain_games import base_game
from brain_games.games.brain_progression import brain_progression_question


def main():
    hello_string = 'What number is missing in the progression?'
    base_game(hello_string=hello_string,
              get_question_function=brain_progression_question)


if __name__ == '__main__':
    main()
