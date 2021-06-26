from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.hideturtle()
        self.penup()
        self.level = 0
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.level += 1
        self.goto(-220, 260)
        self.write(f"Level: {self.level}", False, align="center", font=(FONT))

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", False, align="center", font=("Arial", 16, "bold"))







