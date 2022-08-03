import turtle as t
from turtle import Turtle, Screen
import random

timmy = Turtle()

t.colormode(255)


def colors():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


# Giving timmy a shape of turtle, i.e calling its method shape
timmy.shape("classic")
timmy.speed("fastest")


def draw_circle(size_gap):
    last_limit = int(360 / size_gap)
    for _ in range(last_limit):
        color = colors()
        timmy.color(color)
        timmy.circle(100)
        timmy.setheading(timmy.heading() + size_gap)


draw_circle(5)
my_screen = Screen()
