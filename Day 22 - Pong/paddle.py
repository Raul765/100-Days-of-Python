from turtle import Turtle, Screen

speed = 20

class Paddle(Turtle):
    def __init__(self,x,y):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_len=5,stretch_wid=1)
        self.seth(90)
        self.setx(x)
        self.sety(y)
        
    def up(self):
       self.forward(speed)

    def down(self):
        self.back(speed)