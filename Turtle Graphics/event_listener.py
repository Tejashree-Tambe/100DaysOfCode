import turtle as t
from turtle import Turtle, Screen
import random

timmy = Turtle()
my_screen = Screen()


def go_ahead():
    timmy.forward(20)


my_screen.listen()
my_screen.onkey(key='space', fun=go_ahead)

my_screen.exitonclick()