from turtle import Turtle, Screen

timmy = Turtle()
my_screen = Screen()


def forward():
    timmy.forward(20)


def backward():
    timmy.backward(20)


def counter_clockwise():
    timmy.left(10)


def clockwise():
    timmy.right(10)


def clear():
    timmy.clear()
    timmy.home()


my_screen.listen()
my_screen.onkey(key='w', fun=forward)
my_screen.onkey(key='s', fun=backward)
my_screen.onkey(key='a', fun=counter_clockwise)
my_screen.onkey(key='d', fun=clockwise)

my_screen.onkey(key='c', fun=clear)

my_screen.exitonclick()