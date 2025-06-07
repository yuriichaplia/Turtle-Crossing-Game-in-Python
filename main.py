import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("The Turtle Crossing Capstone Project")
screen.tracer(0)

player_1 = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.listen()
screen.onkeypress(player_1.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_cars()
    car_manager.movement_of_the_cars()

    for car in car_manager.all_cars:
        if player_1.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False

    if player_1.finish_line():
        scoreboard.increase_score()
        car_manager.increase_speed()


screen.exitonclick()
