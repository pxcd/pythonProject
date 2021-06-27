from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0

        # self.high_score = open("data.txt")
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(-20, 270)
        self.clear()
        self.show_scoreboard()

    def show_scoreboard(self):
        self.clear()
        self.write(f"Score : {self.score}  High Score : {self.high_score}", False, align="center", font=("Arial", 16, "bold"))

    def increment(self):
        self.clear()
        self.score = self.score + 1
        self.show_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"GAME OVER", False, align="center", font=("Arial", 16, "bold"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.show_scoreboard()





