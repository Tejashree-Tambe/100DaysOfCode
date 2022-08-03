from turtle import Turtle, Screen

# Making obj of Turtle class, here obj is timmy
timmy = Turtle()
print(timmy)

# Giving timmy a shape of turtle, i.e calling its method shape
timmy.shape("turtle")

# Giving color to obj timmy
timmy.color("blue")

# Move timmy
timmy.forward(100)


# Making obj of Screen to fit the turtle
my_screen = Screen()

# Checking attribute canvas height of obj
print(my_screen.canvheight)

# on clicking anywhere the screen should be exited, i.e calling a method exitonclick() of Screen class
my_screen.exitonclick()
