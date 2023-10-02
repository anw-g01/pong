from turtle import Screen, Turtle
from config import *
import random


class Paddle(Turtle):
    """
    Inherits the Turtle class from the turtle module to represent each player's paddle in the Pong game.

    args:
    pos - initial starting position of the paddle

    attributes (all inherited):
    shape -  shape of the paddle
    speed -  speed of the paddle's movement
    color -  color of the paddle
    shapesize - uses integer parameters, PADDLE_WIDTH and PADDLE_HEIGHT,
    to stretch the size into a classic rectangular paddle shape.
    """

    def __init__(self, pos):
        super().__init__(shape="square")
        self.penup()
        self.speed(PADDLE_SPEED)
        self.color(PADDLE_COLOUR)
        self.shapesize(  # all turtles start as 20 x 20
            stretch_wid=PADDLE_WIDTH / 20,
            stretch_len=PADDLE_HEIGHT / 20
        )
        self.setpos(pos)

    def move_up(self):
        """
        Shifts the paddle upwards by a specified value of SHIFT_DISTANCE given it is within the
        screen height bounds. Uses key dimensions from config.py to ensure parameterised limits.
        """
        if self.ycor() + PADDLE_WIDTH / 2 + BOUND_TOLERANCE < SCREEN_HEIGHT / 2:
            self.goto(self.xcor(), self.ycor() + SHIFT_DISTANCE)

    def move_down(self):
        """
        Shifts the paddle downwards by a specified value of SHIFT_DISTANCE given it is within the
        screen height bounds. Uses key dimensions from config.py to ensure parameterised limits.
        """
        if self.ycor() - PADDLE_WIDTH / 2 - BOUND_TOLERANCE > -SCREEN_HEIGHT / 2:
            self.goto(self.xcor(), self.ycor() - SHIFT_DISTANCE)


class Ball(Turtle):
    """
    Inherits the Turtle class from the turtle module to represent each player's paddle in the Pong game.

    args:
    pos - initial starting position of the ball

    attributes (all inherited):
    shape -  shape of the paddle
    speed -  speed of the ball's movement
    color -  color of the ball
    shapesize - uses integer parameters, BALL_WIDTH and BALL_HEIGHT,
    to resize the ball into a desired spherical size.
    """

    def __init__(self):
        super().__init__(shape="circle")
        self.penup()
        self.speed(BALL_SPEED)
        self.color(BALL_COLOUR)
        self.shapesize(
            stretch_wid=BALL_WIDTH / 20,
            stretch_len=BALL_HEIGHT / 20)
        self.setpos(0, 0)

    def reset_pos(self):
        """Resets the position of the ball to the centre of the screen used after each round of play."""
        self.setpos(0, 0)

    def start_heading(self, last_side, first_play=False):
        """
        Sets a random starting heading direction for the start of a new round within specified angle ranges.
        Ensures that the ball moves toward the opposite side of the player who lost the previous round.

        args:
        last_side (int) - represents the x-coordinate from the final position of the ball before going out
         of bounds. Used to last check which side ball was last out-of-bounds
        first_play (bool) - used to pick a random starting side (left/right) if it's the first round of play.
        """
        left, right = [(120, 150), (210, 240)], [(30, 60), (300, 330)]
        sides = (random.choice(left), random.choice(right))
        if not first_play:
            if last_side < 0:  # if gone out left side
                chosen_side = sides[1]  # right side
            else:
                chosen_side = sides[0]
            heading = random.randint(chosen_side[0], chosen_side[1])
        else:
            chosen_side = random.choice(sides)
            heading = random.randint(chosen_side[0], chosen_side[1])
        self.setheading(heading)

    def move(self):
        """
        Uses the .forward() method from the turtle module to move the ball object forward in its current heading
        direction, pre-determined by the start_heading() method. Incremented using BALL_MOVE_STEP (int).
        """
        self.forward(BALL_MOVE_STEP)

    def vertical_bounce(self):
        """
        Orients the heading of the ball to mimic a reflection bounce from a vertical surface (i.e. paddles).
        """
        self.right(2 * self.heading())

    def horizontal_bounce(self):
        """
        Re-orients the heading of the ball to mimic a reflection bounce
        from a horizontal surface (i.e. top and bottom screen edge).
        """
        self.right(2 * self.heading() - 180)

    def hit_wall(self):
        """Checks if the ball has collided with the top or bottom edge of the screen."""
        return abs(self.ycor()) > (SCREEN_HEIGHT / 2) - BALL_WIDTH

    def hit_left_paddle(self, paddle_obj):
        """
        Checks if the ball has collided with the left paddle. Uses two conditions that must be met:
        1. the x-coordinate of the ball is smaller than the x-coordinate of the given paddle,
        2. the distance between the paddle object and ball is within half the length of the given paddle.
        """
        return (self.xcor() < (L_PADDLE_X_POS + PADDLE_HEIGHT + BALL_WIDTH / 2)
                and self.distance(paddle_obj) < (BALL_WIDTH + PADDLE_WIDTH / 2))

    def hit_right_paddle(self, paddle_obj):
        """
        Checks if the ball has collided with the right paddle. Uses two conditions that must be met:
        1. the x-coordinate of the ball is greater than the x-coordinate of the given paddle,
        2. the distance between the paddle object and ball is within half the length of the given paddle.
        """
        return (self.xcor() > (R_PADDLE_X_POS - PADDLE_HEIGHT - BALL_WIDTH / 2)
                and self.distance(paddle_obj) < (BALL_WIDTH + PADDLE_WIDTH / 2))

    def out_of_bounds(self):
        """
        Checks if the ball has gone out of bounds, i.e. past the paddles on either the
        left or right side and towards the edge of the screen window. Returns True if so.
        """
        return abs(self.xcor()) > (SCREEN_WIDTH / 2) - BALL_WIDTH


class Scoreboard(Turtle):
    """
    Inherits the Turtle class from the turtle module to display text as the scoreboard for the pong game.

    args:
    player_names - tuple(str, str) stores player names for the left and right side

    non-inherited attributes:
    left_score - score of the left player at current time
    right_score - score of the right player at current time
    players - tuple storing player names from the player_names input argument
    """

    def __init__(self, player_names):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.left_score = 0
        self.right_score = 0
        self.players = player_names
        self.display_points()
        self.display_names()

    def reset_score(self):
        """Resets each player's current score to zero for a new game."""
        self.left_score = 0
        self.right_score = 0

    def left_player_points(self):
        """Displays left player's score on the left side of the screen."""
        self.goto(L_SCORE_ALIGNMENT)
        self.write(
            self.left_score,
            align=ALIGNMENT,
            font=FONTS_T
        )

    def right_player_points(self):
        """Displays right player's score on the right side of the screen."""
        self.goto(R_SCORE_ALIGNMENT)
        self.write(
            self.right_score,
            align=ALIGNMENT,
            font=FONTS_T
        )

    def display_names(self):
        """Displays both player's names above each score."""
        self.goto(L_NAME_POS)
        self.write(
            self.players[0],
            align=ALIGNMENT,
            font=FONTS_N
        )
        self.goto(R_NAME_POS)
        self.write(
            self.players[1],
            align=ALIGNMENT,
            font=FONTS_N
        )

    def display_points(self):
        """Clears current text display and calls all display methods in one function."""
        self.clear()
        self.left_player_points()
        self.right_player_points()
        self.display_names()

    def display_winner(self):
        """Displays the winner name at the centre of the screen after a finished game and resets the score."""
        self.goto(0, 0)
        if self.left_score > self.right_score:
            winner = self.players[0]
        else:
            winner = self.players[1]
        self.write(
            f"{winner} wins!",
            align=ALIGNMENT,
            font=(FONT_NAME, 40, FONT_STYLE)
        )
        self.reset_score()

