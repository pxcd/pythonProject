from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, coordinates):
        super().__init__()
        self.goto(coordinates)
        self.color("white")
        self.shape("square")
        self.penup()
        self.turtlesize(stretch_len=5, stretch_wid=1)
        self.speed(0)
        self.setheading(90)

    def move_up(self):
        self.forward(20)


    def move_down(self):
        self.backward(20)




