from player import Player
import time
from turtle import Screen
from scoreboard import Scoreboard
from car_manager import CarManager


screen = Screen()
screen.setup(width=600, height=600)
screen.listen()
screen.tracer(0)

scoreboard = Scoreboard()
player = Player()
car_manager = CarManager()

screen.onkey(player.move, "Up")


game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.car_move()



    if player.ycor() == 280:
        car_manager.car_reset()
        player.reset()
        scoreboard.update_scoreboard()

    # collision detection
    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False


screen.exitonclick()