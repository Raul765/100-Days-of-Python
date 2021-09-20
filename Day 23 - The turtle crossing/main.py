import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
screen.listen()
screen.onkey(player.move,"Up")

scoreboard = Scoreboard()
car_manager = CarManager()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.manage_cars()

    #End of the level
    if player.ycor() >= 280:
        player.refresh()
        scoreboard.update()
        car_manager.speed_up()

    #Detect game over
    for car in car_manager.cars:
        if car.distance(player)<20:
            scoreboard.game_over()
            game_is_on=False


screen.exitonclick()