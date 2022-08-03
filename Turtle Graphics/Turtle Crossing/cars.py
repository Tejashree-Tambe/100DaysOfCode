from turtle import Turtle
import random
import turtle as t
t.colormode(255)

STARTING_MOVE_DISTANCE = 5
SPEED_INCREMENT = 10


def y_cor():
    return random.randint(-220, 220)


def colors():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


class Cars:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle(shape='square')
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(colors())
            new_car.penup()
            new_car.goto(400, y_cor())
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def increase_car_speed(self):
        self.car_speed += SPEED_INCREMENT

