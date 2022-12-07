# Uses the turtle module to create the scoreboard.
from turtle import Turtle

# Variable is used to store the font details.
FONT = ("Courier", 24, "normal")

# Class inherits from the turtle module.


class Scoreboard(Turtle):

    # Creates the properties of the scoreboard and also creates the text for the element.
    def __init__(self):
        super().__init__()
        self.score = 1
        self.color("black")
        self.hideturtle()
        self.penup()
        self.update_scoreboard()

    # Provides the location of the scoreboard and the text.
    def update_scoreboard(self):
        self.goto(-280, 260)
        self.write(f"Level: {self.score}", align="left", font=FONT)

    # Increases the score while removing the current text and replacing it with the updated text.
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    # repositions to the center of the screen and creates the game over text.
    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=FONT)
