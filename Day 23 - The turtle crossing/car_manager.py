from turtle import Turtle
from random import randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.move_distance = STARTING_MOVE_DISTANCE
        self.cars=[]

    def manage_cars(self):
        if randint(1,6)==1:
            self.create_cars()
        self.move_cars()
        self.delete_cars()


    def create_cars(self):
        car=Turtle()
        car.penup()
        car.seth(180)
        car.shape("square")
        car.shapesize(stretch_len=2)
        car.color(COLORS[randint(0,5)])
        car.setx(320)
        y=(randint(-26,26))
        if y%2==0 and y<=0:
            y+=1
        elif y%2==0 and y>0:
            y-=1
        car.sety(y*10)
        self.cars.append(car)

    def move_cars(self):
        for car in self.cars:
            car.forward(self.move_distance)

    def delete_cars(self):
        if len(self.cars)>0:
            if self.cars[0].xcor()<=-320:
                self.cars[0].hideturtle()
                self.cars.pop(0)

    def speed_up(self):
        self.move_distance += MOVE_INCREMENT
