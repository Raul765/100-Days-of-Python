from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food

    if snake.head.distance(food) < 10:
        snake.extend()
        food.refresh()
        scoreboard.update()
     
     # Detect collision with wall
    if abs(snake.head.xcor()) > 300 or abs(snake.head.ycor()) > 300:
        game_is_on=False
        scoreboard.game_over()

     # Detect collision with tail    
    for i in snake.body[1:]:
        if snake.head.distance(i) < 10:
            game_is_on=False
            scoreboard.game_over()


screen.exitonclick()