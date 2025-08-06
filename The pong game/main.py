from turtle import Screen
from move_paddle import Paddle
import time
from ball import Ball
from scoreboard import Scoreboard
screen=Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("The Pong Game :)")
r_paddle=Paddle(x1=370,y1=0)
l_paddle=Paddle(x1=-375,y1=0)
screen.tracer(0)
screen.listen()
ball=Ball()
scoreboard=Scoreboard()
screen.onkey(key="Up",fun=r_paddle.move_up)
screen.onkey(key="Down",fun=r_paddle.move_down)
screen.onkey(key="w",fun=l_paddle.move_up)
screen.onkey(key="s",fun=l_paddle.move_down)
is_game_on= True
while is_game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move_up()
    ##detect collosion with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if r_paddle.distance(ball) < 50 and ball.xcor() > 340 or l_paddle.distance(ball) < 50 and ball.xcor() < -350:
        ball.bounce_x()
    if ball.xcor() > 380:
        ball.home()
        scoreboard.right_win()
        ball.move_oppostie()
    if ball.xcor() <-380:
        ball.home()
        scoreboard.left_win()
        ball.again()


















screen.exitonclick()
