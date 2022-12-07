# Uses the datetime & turtle module create the screen and limit the refresh rate
# to the specified amount.
import time
from turtle import Screen

# Calls the classes from the other python files.
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Sets the screen size and stops automatic screen updates.
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Sets variables with classes.
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

# Sets up the screen to register the player controls.
screen.listen()
screen.onkey(player.up, "Up")

# A boolean to control the while loop.
game_is_on = True

# A loop that will run for as long as the game over condition isn't met.
while game_is_on:

    # Updates the positions on the screen every loop.
    time.sleep(0.1)
    screen.update()

    # Creates a chance for a car object to be created.
    car_manager.create_car()

    # Moves all car objects every loop.
    car_manager.move_cars()

    # Checks to see if the player and car objects are interacting. This
    # changes the game loop to false and provides the game over scoreboard.
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # If the player makes it to the top of the screen the player is moved back to
    # the bottom of the screen and the score/car speed is increased.
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_score()

# Once the loop has ended by a car object interacting with the player object
# the user can close the program by using a mouse button anywhere on the screen.
screen.exitonclick()
