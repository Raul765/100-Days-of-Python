from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("black")
        self.hideturtle()
        self.goto(-295,265)
        self.level=0
        self.update()

    def update(self):
        self.clear()
        self.level += 1
        self.write(f"Level: {self.level}",align="left",font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER",align="left",font=FONT)