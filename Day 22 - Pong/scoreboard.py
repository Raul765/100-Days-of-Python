from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.right_score=0
        self.left_score=0
        self.refresh()

    def refresh(self):
        self.clear()
        self.goto(-100,200)
        self.write(f"{self.left_score}", align="center", font=("courier",80,"normal"))
        self.goto(100,200)
        self.write(f"{self.right_score}", align="center", font=("courier",80,"normal"))

    def point_for_right(self):
        self.right_score+=1
        self.refresh()

    def point_for_left(self):
        self.left_score+=1
        self.refresh()
    