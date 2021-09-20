from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()

screen.bgcolor("Black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

scoreboard = Scoreboard()
right_paddle = Paddle(350,0)
left_paddle = Paddle(-350,0)
ball = Ball()


screen.listen()
screen.onkey(right_paddle.up,"Up")
screen.onkey(right_paddle.down,"Down")
screen.onkey(left_paddle.up,"w")
screen.onkey(left_paddle.down,"s")

game_is_on = True

while game_is_on:
    screen.update()
    ball.move()
    
    #Detect collision with wall
    if abs(ball.ycor())>= 290:
        ball.bounce()

    #Detect collision with right paddle
    if ball.xcor()>=330 and ball.xcor()<=370 and abs(ball.ycor()-right_paddle.ycor())<=49:
        ball.bounce()

    #Detect collision with left paddle
    if ball.xcor()<=-330 and ball.xcor()>=-370 and abs(ball.ycor()-left_paddle.ycor())<=49:
        ball.bounce()

    #Detect ball out of bounds
    if abs(ball.xcor())>=410:
        if ball.xcor()>0:
            scoreboard.point_for_left()
        else:
            scoreboard.point_for_right()
        ball.refresh()
    
screen.exitonclick()