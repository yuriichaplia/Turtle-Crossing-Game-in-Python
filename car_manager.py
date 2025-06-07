import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:
    def __init__(self):
        self.all_cars = []
        self.speed_value = STARTING_MOVE_DISTANCE

    def create_cars(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.goto(x=315, y=random.randint(-250, 250))
            new_car.color(random.choice(COLORS))
            self.all_cars.append(new_car)

    def movement_of_the_cars(self):
        for car in self.all_cars:
            car.backward(self.speed_value)
        self.all_cars = [car for car in self.all_cars if car.xcor() > -320]

    def increase_speed(self):
        self.speed_value += MOVE_INCREMENT



