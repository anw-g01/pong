# Pong

A classic pong game implemented using the Turtle graphics module in Python.

## Project Files
1. `main.py`: Main script that initialises the game and handles user input for player names and replay prompts.
2. `config.py`: Stores configuration parameters (global variables) for the game, allowing customisation across nearly every aspect.
3. `gameplay.py`: Manages the main game logic by handling ball movement, collisions and rounds by utilising objects, attributes and methods.
4. `classes.py`: Contains definitions of classes to represent the paddles, ball and scoreboard for the pong game for use in the main game logic.

## How to play
1. Run `main.py` to start the program.
2. Enter the names of two players in the command line prompt.
3. Paddle key bind controls are set to "`W`" and "`S`" for the left player and the `up` and `down` arrow keys for the right player (can be changed to preference if required in `config.py`).
4. Bounce the moving ball with paddles until a player misses and the ball reaches out of bounds.
5. The game ends with either a win or a draw depending on the specified number of rounds to play (default is 3 rounds but can be changed in `config.py`)
6. Can decide to play a new game with the same number of rounds or exit the program.


