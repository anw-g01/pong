
SPEEDS = {
    5: "fastest",
    4: "fast",
    3: "normal",
    2: "slow",
    1: "slowest"
}

# ============ GAME WINDOW ============ #
ROUNDS = 3   # no. of total rounds to play (best of)
WINDOW_TITLE = "Pong"
SCREEN_COLOUR = "black"
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800

# ============ BALL ============ #
TIME_STEP = 0.001   # "refresh rate" for each frame of the game
TIME_STEP_DECREMENT = 0.7   # => increase in ball speed, set as 1 for no speed change
BALL_COLOUR = "yellow"
BALL_SPEED = SPEEDS[5]
BALL_MOVE_STEP = 1  # value of 1 for the smoothest animations
BALL_WIDTH = 12
BALL_HEIGHT = 12
BALL_X_POS = 0
BALL_Y_POS = 0

# ======================== PADDLES ======================== #

# ------ PADDLE ------ #
PADDLE_COLOUR = "white"
PADDLE_WIDTH = 150
PADDLE_HEIGHT = 5
PADDLE_SPEED = SPEEDS[5]

# ------ PADDLE LOCATION ------ #
R_PADDLE_X_POS = (SCREEN_WIDTH / 2) - 100
R_PADDLE_Y_POS = 0
L_PADDLE_X_POS = - R_PADDLE_X_POS    # design symmetry
L_PADDLE_Y_POS = 0

# ------ PADDLE MOVEMENT ------ #
SHIFT_DISTANCE = 50
BOUND_TOLERANCE = 10
R_PADDLE_UP = "Up"      # keybindings for gameplay movement
R_PADDLE_DOWN = "Down"
L_PADDLE_UP = "w"
L_PADDLE_DOWN = "s"

# ============ TEXT ============ #
TEXT_COLOUR = "white"
FONT_NAME = "Courier New"
FONT_SIZE = 30
FONT_STYLE = "normal"
FONTS_T = (FONT_NAME, FONT_SIZE, FONT_STYLE)
ALIGNMENT = "center"
L_SCORE_ALIGNMENT = (- SCREEN_WIDTH / 4, SCREEN_HEIGHT / 2 - 150)
R_SCORE_ALIGNMENT = (SCREEN_WIDTH / 4, SCREEN_HEIGHT / 2 - 150)

# ----- NAMES ----- #
NAME_FONT_SIZE = 15
FONTS_N = (FONT_NAME, NAME_FONT_SIZE, FONT_STYLE)
L_NAME_POS = (L_SCORE_ALIGNMENT[0], L_SCORE_ALIGNMENT[1] + 50)
R_NAME_POS = (R_SCORE_ALIGNMENT[0], R_SCORE_ALIGNMENT[1] + 50)


