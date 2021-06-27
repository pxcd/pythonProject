import time
from turtle import Screen
from snek import Snek
from food import Food
from scoreboard import ScoreBoard

##
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snek Gaem")
screen.tracer(0)
#

snek = Snek()
food = Food()
screen.listen()
scoreboard = ScoreBoard()

screen.onkey(snek.up, "Up")
screen.onkey(snek.down, "Down")
screen.onkey(snek.left, "Left")
screen.onkey(snek.right, "Right")


game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    snek.move()
    # detect collision with food
    if snek.head.distance(food) < 15:
        food.refresh()
        scoreboard.increment()
        snek.extend()

    # detect wall collision
    if snek.head.xcor() > 280 or snek.head.xcor() < -280 or snek.head.ycor() > 280 or snek.head.ycor() < -280:
        scoreboard.reset()
        snek.reset()
        # scoreboard.game_over()
        # game_is_on = False

    # detect tail collision
    # if head collides with any segment, game over
    for segment in snek.segments[1:]:
        # if segment == snek.head:
        #     pass
        # elif snek.head.distance(segment) < 10:
        #     game_is_on = False
        #     scoreboard.game_over()
        if snek.head.distance(segment) < 10:
            scoreboard.reset()
            snek.reset()
            # game_is_on = False
            # scoreboard.game_over()



screen.exitonclick()