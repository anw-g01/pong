from turtle import Screen
from classes import Paddle, Ball, Scoreboard
from config import *
import time


class Pong:
    """
    Represent the pong game.

    args:
    player_names (tuple(str, str)) - tuple containing player names for the left and right side

    attributes:
    window_frame - game window screen created as Screen() object from the turtle module
    ball - Ball() object from classes.py
    paddles (dict) - dictionary containing Paddle() objects for each player
    rounds_to_play (int) - number of rounds played in one game
    current_round (int) - current round of the game at current time
    side_lost (int) - the x-coordinate of the side where the ball was last out of bounds
    scoreboard - Scoreboard() object from classes.py
    ball_speed (float) - the frame updating speed of the game
    """
    def __init__(self, player_names):
        self.window_frame = self.setup_window()
        self.ball = Ball()
        self.paddles = {
            "right": Paddle((R_PADDLE_X_POS, R_PADDLE_Y_POS)),
            "left": Paddle((L_PADDLE_X_POS, L_PADDLE_Y_POS))
        }
        self.rounds_to_play = ROUNDS
        self.current_round = 0
        self.side_lost = 0
        self.scoreboard = Scoreboard(player_names)
        self.ball_speed = TIME_STEP

    @staticmethod
    def setup_window():
        """
        Initialises the game window as a Screen() object from the turtle module.
        Command function .tracer(0) turns of turtle tracing movements.
        """
        screen = Screen()
        screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
        screen.title(WINDOW_TITLE)
        screen.bgcolor(SCREEN_COLOUR)
        screen.tracer(0)
        return screen

    def right_paddle_controls(self):
        """Configures keybindings for controlling the right paddle"""
        self.window_frame.onkey(self.paddles["right"].move_up, R_PADDLE_UP)
        self.window_frame.onkey(self.paddles["right"].move_down, R_PADDLE_DOWN)

    def left_paddle_controls(self):
        """Configures keybindings for controlling the left paddle"""
        self.window_frame.onkey(self.paddles["left"].move_up, L_PADDLE_UP)
        self.window_frame.onkey(self.paddles["left"].move_down, L_PADDLE_DOWN)

    def setup_controls(self):
        """Sets up keyboard controls for both paddles in one function call."""
        self.window_frame.listen()
        self.right_paddle_controls()
        self.left_paddle_controls()

    def new_ball(self):
        """
        Resets the ball position for a new round after going out of bounds. If it is the first round,
        the heading is completely randomised, otherwise .start_heading() randomises the angle range
        within the opposite side to which the ball last went out of bounds.
        """
        self.ball.reset_pos()
        if self.current_round == 0:
            self.ball.start_heading(self.side_lost, first_play=True)
        else:
            self.ball.start_heading(self.side_lost)

    def round_over(self):
        """Returns True if the round is over."""
        return self.ball.out_of_bounds()

    def move_ball(self):
        """
        Controls the forward movement of the balls while detecting for collisions and updating the animation
        frames in a continuous loop until the ball reaches out-of-bounds. If loop is broken, round number is
        updated, ball speed is reset and scoreboard is updated.
        """
        while not self.round_over():
            self.ball.move()
            if self.ball.hit_wall():
                self.ball.vertical_bounce()
            elif self.ball.hit_left_paddle(self.paddles["left"]):
                self.ball.horizontal_bounce()
                self.increase_speed()       # increase speed after each paddle bounce with specified increment
            elif self.ball.hit_right_paddle(self.paddles["right"]):
                self.ball.horizontal_bounce()
                self.increase_speed()
            self.window_frame.update()
            time.sleep(self.ball_speed)
        # current_round over:
        self.current_round += 1
        self.ball_speed = TIME_STEP
        self.side_lost = self.ball.xcor()
        self.update_scoreboard()

    def increase_speed(self):
        """
        Increases the refresh rate of the game equivalent to speeding
        up the motion of the ball after every paddle collision.
        """
        self.ball_speed *= TIME_STEP_DECREMENT

    def update_scoreboard(self):
        """Updates attributes and the scoreboard on the outcome of each round."""
        if self.side_lost < 0:
            self.scoreboard.right_score += 1
        elif self.side_lost > 0:
            self.scoreboard.left_score += 1
        self.scoreboard.display_points()

    def play_again(self):
        """User prompt window on whether to play another new game."""
        while True:
            ans = self.window_frame.textinput(
                title="GAME OVER",
                prompt="\nPlay again? (y/n): "
            ).lower()
            if ans in ["y", "n"]:
                return ans == "y"  # True if yes
            print("Error. Try again.")
