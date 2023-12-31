import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()

screen.setup(width=600, height=600)

screen.tracer(0)

player = Player()
car = CarManager()
score=Scoreboard()

screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move()

    for cars in car.all_cars:
        if cars.distance(player) < 23:
            game_is_on = False
            score.game_over()


    if player.finish_point():
         player.go_to_start()
         car.leve_up_game()
         score.increse_leve()



screen.exitonclick()
