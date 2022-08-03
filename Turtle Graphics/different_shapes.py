from turtle import Turtle, Screen
import random

timmy = Turtle()
print(timmy)

# Giving timmy a shape of turtle, i.e calling its method shape
timmy.shape("arrow")

# Giving color to obj timmy
timmy.color("blue")

colors = ['sandy brown', 'orange', 'dark orange', 'chocolate', 'firebrick', 'brown', 'dark red', 'maroon',
          'antique white', 'papaya whip']

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

# Move timmy
for side in range(3, 11):
    angle = 360 / side
    color = random.choice(colors)
    for sides in range(side):
        timmy.color(color)
        timmy.forward(100)
        timmy.left(angle)


# Making obj of Screen to fit the turtle
my_screen = Screen()

# on clicking anywhere the screen should be exited, i.e calling a method exitonclick() of Screen class
my_screen.exitonclick()
