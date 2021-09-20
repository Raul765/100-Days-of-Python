from turtle import Turtle
from types import DynamicClassAttribute
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("Day24\Improved snake\data.txt") as data:
            self.highscore = int(data.read())
        self.color("white")
        self.penup()
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(0, 265)
        self.write(f"Score: {self.score}    Highscore: {self.highscore}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        if self.score > self.highscore:
            self.highscore = self.score
            with open("Day24\Improved snake\data.txt",mode="w") as data:
                data.write(str(self.highscore))
        self.update_scoreboard()
        self.clear()

    def reset_scoreboard(self):
        self.score=0
        self.clear()
        self.update_scoreboard()


    
