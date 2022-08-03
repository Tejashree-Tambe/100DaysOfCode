from turtle import Screen
from tortoise import Tortoise
from cars import Cars
from levels import Levels
import time

is_game_on = True

screen = Screen()
screen.title('Turtle Crossing')
screen.setup(width=800, height=600)
screen.tracer(0)

tortoise = Tortoise()

cars = Cars()

levels = Levels()

screen.listen()
screen.onkey(tortoise.move_up, 'Up')

while is_game_on:
    time.sleep(0.1)
    screen.update()

    cars.create_car()
    cars.move_cars()

    for car in cars.all_cars:
        # detect collision of turtle with car:
        if car.distance(tortoise) < 20:
            is_game_on = False
            levels.game_over()

        # detect collision of turtle at the end of road
        if tortoise.ycor() > 280:
            tortoise.go_to_start()
            cars.increase_car_speed()
            levels.increase_level()

screen.exitonclick()