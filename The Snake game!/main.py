from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreborad
screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("The Snake Game!")
screen.tracer(0)## to on and offf the animation
screen.listen()
snake = Snake()
food=Food()
scoreboard=Scoreborad()
screen.onkey(key="Up",fun=snake.up)
screen.onkey(key="Down",fun=snake.down)
screen.onkey(key="Right",fun=snake.right)
screen.onkey(key="Left",fun=snake.left)

is_game_on=True
while is_game_on:
    screen.update()
    time.sleep(0.1)##it means wait for 0.1 sec and then refresh the screen
    snake.move()
    #Detect coiilsion with the food
    if snake.segment[0].distance(food)<15:
        food.refresh()
        snake.extend()
        scoreboard.add_score()
    #Detect collosion with the wall
    if snake.segment[0].xcor()>290 or snake.segment[0].xcor()<-290 or snake.segment[0].ycor()>280 or snake.segment[0].ycor()<-290:
        scoreboard.reset_score()
        snake.reset()
    #Detect collosion with the tail
    #if talis collides with any of the segments
    #is_game_on =False
    ## list slicing
    for segment in snake.segment[1:]:
        # if segment==snake.segment[0]:
        #     pass  ##not to do anything just pass in this case
        if snake.head.distance(segment)<10:
            scoreboard.reset_score()
            snake.reset()



screen.exitonclick()
