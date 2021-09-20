import turtle 
import random

timmy=turtle.Turtle()
timmy.shape("turtle")
timmy.color("black")
turtle.colormode(255)
timmy.speed(10)
timmy.pensize(8)

angles=[0,90,180,270]

for steps in range (150):
    timmy.pencolor(random.randint(0,255),random.randint(0,255),random.randint(0,255))
    timmy.rt(random.choice(angles))
    timmy.fd(25)



screen=turtle.Screen()
screen.exitonclick()


