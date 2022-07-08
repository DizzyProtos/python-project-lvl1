### Hexlet tests and linter status:
[![Actions Status](https://github.com/DizzyProtos/python-project-lvl1/workflows/hexlet-check/badge.svg)](https://github.com/DizzyProtos/python-project-lvl1/actions)

### Code Climate badge
[![Maintainability](https://api.codeclimate.com/v1/badges/00dbf89aa693fe6a786c/maintainability)](https://codeclimate.com/github/DizzyProtos/python-project-lvl1/maintainability)


### Requirements
- python >=3.*
- poetry

### Installation
- make install - to install dependencies using poetry
- make build - to build the source and wheels archives
- make package-install - to install the games package in your home directory
- *game name* - to run any game after installing the brain_games package

You can run any game without installing games package:
- "make *game name*"


### Project description
*games/* - Directory with games logic:
- *games/brain_main.py* - module with general game flow
-- *run_game(game)* - runs a game from the module. The module must have: <br/>
    string *HELLO_MESSAGE* to greet the player <br/>
    function *get_question_with_answer* to get question string and a correct answer

- each game has its own module with this game's data and logic

*scripts/* - Directory with scripts that launch games. Each module imports a game and calls *brain_main.run_brain_game(game)* to launch this game.



### Gameplay recordings

brain-even:
https://asciinema.org/a/C9wxIDjlIcyCQ4bmEwaSlKOpD

brain-calc:
https://asciinema.org/a/jzWURE25xr0E2FStIGKtCXOvt

brain-gcd:
https://asciinema.org/a/jzWURE25xr0E2FStIGKtCXOvt

brain-progression:
https://asciinema.org/a/twxjDuvT2YMbyVim790Mx0HWS

brain-prime:
https://asciinema.org/a/56RdXdXNfTwaqKZgRQSLEeMVb