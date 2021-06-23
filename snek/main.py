import time
from turtle import Screen
from snek import Snek


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snek Gaem")
screen.tracer(0)


snek = Snek()
screen.listen()


screen.onkey(snek.up, "Up")
screen.onkey(snek.down, "Down")
screen.onkey(snek.left, "Left")
screen.onkey(snek.right, "Right")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snek.move()
    # snek.up()


screen.exitonclick()