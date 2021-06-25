from turtle import Turtle

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.r_score = 0
        self.l_score = 0
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(f"{self.l_score}", False, align="center", font=("Arial", 80, "bold"))
        self.goto(100, 200)
        self.write(f"{self.r_score}", False, align="center", font=("Arial", 80, "bold"))


    def r_point(self):
        self.r_score = self.r_score + 1
        self.update_scoreboard()

    def l_point(self):
        self.l_score = self.l_score + 1
        self.update_scoreboard()


