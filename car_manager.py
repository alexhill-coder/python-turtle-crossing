# Uses the turtle module to create the car objects.
from turtle import Turtle

# Uses the random module to create instances of the car object at various positions and times.
import random

# The variables store the car object colors which is chosen at random upon creation,
# the starting move distance and the amount to increase the speed.
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    # Creates the list variable and the initial movement distance.
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    # Every refresh of the screen has a 1 in 6 chance to create a car object.
    def create_car(self):
        random_chance = random.randint(1, 6)

        # Should the number from the random_chance variable = 1 a new instance
        # of a car object is made with a random color and position along the y axis.
        # They are then appended to the all_cars variable.
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.goto(300, random.randint(-250, 250))
            self.all_cars.append(new_car)

    # Moves all the car objects by the amount specified in the car_speed variable.
    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    # Increases the movement speed of the car objects set by the Move_Increment variable.
    def level_up(self):
        self.car_speed += MOVE_INCREMENT
