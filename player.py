# Uses the turtle module to create the player.
from turtle import Turtle

# Variables used to store the starting position, how much the player can move per button press
# and the location of the edge of the screen.
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

# A class that inherits from the turtle module.


class Player(Turtle):

    # Provides the properties of the player object, sets the direction and the function to set
    # location.
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.go_to_start()

    # Sets the distance the player moves.
    def up(self):
        self.forward(MOVE_DISTANCE)

    # Sets the starting position.
    def go_to_start(self):
        self.goto(STARTING_POSITION)

    # Checks to see if the player is at the top of the screen.
    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
