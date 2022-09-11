from turtle import Screen, xcor, ycor
from ball import Ball
from paddle import Paddle
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    # Collision with top and bottom walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Collision with right paddle
    if ball.distance(r_paddle) < 50 and \
            ball.xcor() > 320 or \
            ball.distance(l_paddle) < 50 and \
            ball.xcor() < -320:
        ball.bounce_x()

    # Detect right miss
    if ball.xcor() > 380:
        ball.reset_position()
        ball.bounce_x()

    # Detect left miss
    if ball.xcor() < -380:
        ball.reset_position()
        ball.bounce_x()

screen.exitonclick()
