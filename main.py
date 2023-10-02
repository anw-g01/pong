
from gameplay import Pong
import os


def clear_screen():
    """Clears the terminal command line window."""
    os.system('cls' if os.name == 'nt' else 'clear')


def input_names():
    """User can input two player names for displaying scores."""
    while True:
        left_player = input("\nPlayer on left: ")
        if left_player.isalpha():
            break
        print("Error. Try again")
    while True:
        right_player = input("\nPlayer on right: ")
        if right_player.isalpha():
            break
    return left_player, right_player


def main():
    game = Pong(input_names())

    while True:
        game.setup_controls()   # initiate keybindings for player paddles
        for i in range(game.rounds_to_play):
            game.new_ball()     # reset ball and set new random heading for a new round
            game.move_ball()    # move the ball and handle collisions with walls, paddles and out of bounds
        game.scoreboard.display_winner()    # display winner after final round

        if not game.play_again():
            break
        game.scoreboard.clear()     # clear all text displays
        game.scoreboard.display_points()    # re-instate player scores

    print("\nThanks for playing!")      # program ended


if __name__ == "__main__":
    main()


