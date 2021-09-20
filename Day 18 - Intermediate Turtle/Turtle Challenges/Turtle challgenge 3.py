import turtle 
import random

timmy=turtle.Turtle()
timmy.shape("turtle")
timmy.color("black")
timmy.pensize(8)
turtle.colormode(255)

timmy.up()
timmy.setx(-50)
timmy.sety(100)
timmy.pendown()

for number_of_sides in range (3,11):
    angle=360/number_of_sides
    timmy.pencolor(random.randint(0,255),random.randint(0,255),random.randint(0,255))

    for i in range(number_of_sides):
        timmy.fd(100)
        timmy.rt(angle)

screen=turtle.Screen()
screen.exitonclick()