from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500,height=400)
colors=["red","orange","yellow","green","blue","purple"]
y=-125

turtles=[]
for i in range (6):
    turtle=Turtle(shape="turtle")
    turtle.color(colors[i])
    turtle.penup()

    turtle.speed(5)
    turtle.goto(-230,y)
    turtle.speed(2)
    
    turtles.append(turtle)

    y+=50

user_bet=screen.textinput(title="Make your bet",prompt="Which turtle will win the race? Enter a color: ")

end_of_race=False

while not end_of_race:
    for turtle in turtles:
        move=random.randint(0,1)
        if move==1:
            turtle.forward(10)
        if turtle.xcor()==230:
            winner=turtle.color()[0]
            end_of_race=True
            break

print(f"The {winner} turtle is the winner.")
if user_bet==winner:
    print("You win!")
else:
    print("You lose!")