import turtle 
import random

timmy=turtle.Turtle()
timmy.shape("turtle")
timmy.color("black")
turtle.colormode(255)
timmy.speed(0)
timmy.pensize(5)

number_of_circles=70
for n in range (number_of_circles):
    timmy.pencolor(random.randint(0,255),random.randint(0,255),random.randint(0,255))
     #draw circle
    timmy.circle(150)  
     #change heading
    timmy.setheading(n*360/number_of_circles)

#hide turtle
timmy.hideturtle()


screen=turtle.Screen()
screen.exitonclick()


