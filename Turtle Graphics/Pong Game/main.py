from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

LEFT_PADDLE_POSITION = (-350, 0)
RIGHT_PADDLE_POSITION = (350, 0)
game_is_on = True

screen = Screen()
screen.title('The Pong Game')
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.tracer(0)

left_paddle = Paddle(LEFT_PADDLE_POSITION)
right_paddle = Paddle(RIGHT_PADDLE_POSITION)

ball = Ball()

scoreboard = Scoreboard()

screen.listen()
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")

screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")


def exit_game():
    global game_is_on
    game_is_on = False


while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()

    ball.move()

    # detect collision with wall:
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collision with paddle:
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # detect when right paddle misses hitting the ball, giving score to left side
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.increase_l_score()

    # detect when left paddle misses hitting the ball, giving score to right side
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.increase_r_score()

    screen.onkey(exit_game, "e")
