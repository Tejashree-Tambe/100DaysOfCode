from turtle import Turtle

ALIGNMENT = 'center'


class Levels(Turtle):
    def __init__(self):
        super().__init__()
        self.color('black')
        self.level = 1
        self.hideturtle()
        self.penup()
        self.update_level()

    def update_level(self):
        self.clear()
        self.goto(-300, 250)
        self.write(f'Level: {self.level}', align='center', font=('Courier', 23, 'normal'))

    def increase_level(self):
        self.level += 1
        self.update_level()

    def game_over(self):
        self.goto(0, 0)
        self.write('GAME OVER', align='center', font=('Courier', 23, 'bold'))
