from turtle import Turtle

speed = 0.15

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.refresh()
        self.angle=1

    def refresh(self):
        self.setx(0)
        self.sety(0)
        self.angle=1

    def move(self):
        if self.angle==1:
            x = self.xcor()+speed
            y = self.ycor()+speed
        elif self.angle==2:
            x = self.xcor()+speed
            y = self.ycor()-speed
        elif self.angle==3:
            x = self.xcor()-speed
            y = self.ycor()-speed
        elif self.angle==4:
            x = self.xcor()-speed
            y = self.ycor()+speed

        self.goto(x,y)

    def bounce (self):
        self.angle+=1
        if self.angle>4:
            self.angle-=4
        