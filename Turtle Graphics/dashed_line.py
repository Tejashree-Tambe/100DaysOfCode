from turtle import Turtle, Screen

timmy = Turtle()
print(timmy)

# Giving timmy a shape of turtle, i.e calling its method shape
timmy.shape("arrow")

# Giving color to obj timmy
timmy.color("blue")

# Move timmy

for _ in range(15):
    timmy.forward(10)
    timmy.penup()
    timmy.forward(10)
    timmy.pendown()


# Making obj of Screen to fit the turtle
my_screen = Screen()

# on clicking anywhere the screen should be exited, i.e calling a method exitonclick() of Screen class
my_screen.exitonclick()