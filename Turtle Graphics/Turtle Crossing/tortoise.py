from turtle import Turtle
MOVING_POSITION = 10
STARTING_POSITION = (0, -280)


class Tortoise(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.go_to_start()

    def move_up(self):
        self.forward(MOVING_POSITION)

    def go_to_start(self):
        self.goto(STARTING_POSITION)

