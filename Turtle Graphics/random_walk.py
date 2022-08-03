from turtle import Turtle, Screen
import random

timmy = Turtle()

# Giving timmy a shape of turtle, i.e calling its method shape
timmy.shape("classic")

# Giving color to obj timmy
timmy.pensize(10)

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

directions = ['North', 'South', 'East', 'West']


def get_direction():
    direct = random.choice(directions)
    if direct == 'North':
        timmy.left(90)

    elif direct == 'South':
        timmy.right(90)

    elif direct == 'West':
        timmy.left(180)

    else:
        timmy.right(0)


# Making obj of Screen to fit the turtle
my_screen = Screen()

for _ in range(200):
    color = random.choice(colours)
    timmy.color(color)
    get_direction()
    timmy.forward(20)

# on clicking anywhere the screen should be exited, i.e calling a method exitonclick() of Screen class
my_screen.exitonclick()

