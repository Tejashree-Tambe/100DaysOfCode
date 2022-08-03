from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 10, 'normal')


class WriteState(Turtle):
    def __init__(self, state, x_pos, y_pos):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(x_pos, y_pos)
        self.clear()
        self.write(f"{state}", align=ALIGNMENT, font=FONT)
