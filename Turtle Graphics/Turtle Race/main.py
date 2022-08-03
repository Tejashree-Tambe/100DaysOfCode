import turtle as t
from turtle import Turtle, Screen
import random

is_race_on = False
my_screen = Screen()
my_screen.setup(width=500, height=400)
user_turtle_color = my_screen.textinput(title='Your Bet', prompt='Decide your color')
all_colors = ['purple', 'blue', 'green', 'yellow', 'orange', 'red']
all_turtles = []

y_position = 170

for turtle_index in range(6):
    y_position -= 50
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(all_colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(-250, y_position)
    all_turtles.append(new_turtle)

if user_turtle_color:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_turtle_color:
                print(f"You Won! The {winning_color} is the winner")
            else:
                print(f"You lost! The {winning_color} is the winner")

        random_dist = random.randint(0, 10)
        turtle.forward(random_dist)


my_screen.exitonclick()
