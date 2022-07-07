from brain_games.scripts.brain_main import base_game
from brain_games.games.brain_progression import hello_string
from brain_games.games.brain_progression import brain_progression_question


def main():
    base_game(hello_string=hello_string,
              get_question_function=brain_progression_question)


if __name__ == '__main__':
    main()
