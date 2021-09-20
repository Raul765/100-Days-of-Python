from turtle import Turtle
move_distance=20
class Snake():

    def __init__(self):
        self.body=[]
        self.create_snake()
        self.head = self.body[0]

    def create_snake(self):
        for i in range(3):
            square = Turtle()
            square.shape("square")
            square.color("white")
            square.penup()
            square.goto(-20*i,0)
            self.body.append(square)

    def move(self):
        for i in range (len(self.body)-1,0,-1):
            self.body[i].setx(self.body[i-1].xcor())
            self.body[i].sety(self.body[i-1].ycor())
        self.head.forward(move_distance)

    def up(self):
        self.head.setheading(90)

    def down(self):
        self.head.setheading(270)

    def left(self):
        self.head.setheading(180)

    def right(self):
        self.head.setheading(0) 
