import turtle
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)

# user_bet = turtle.textinput(title="Make your bet", prompt="Who will win?")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

#
# leonardo = Turtle(shape="turtle")
# leonardo.penup()
# leonardo.goto(x=-230, y=-100)

for color in len(colors):
    color = Turtle(shape="turtle")
    color.color(color)


# donatello = Turtle(shape="turtle")
#
#
# michaelangelo = Turtle(shape="turtle")
#
#
# rafael = Turtle(shape="turtle")





screen.exitonclick()



