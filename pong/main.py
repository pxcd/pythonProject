from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time





screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG")
screen.listen()
screen.tracer(0)




l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))


screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")

screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")

ball = Ball()
scoreboard = ScoreBoard()

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    ball.move()
    screen.update()

    # detect wall collision
    if ball.ycor() > 280 or ball.ycor() < -280:
        #needs to bound
        ball.bounce_y()
    # detect collision with  paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # detect when paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()



screen.exitonclick()