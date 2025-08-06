from turtle import Turtle
MOVING_DISTANCE_Y=50
class Paddle(Turtle):

    def __init__ (self,x1,y1):
        super().__init__()
        self.penup()
        self.goto(x=x1, y=y1)
        self.create_paddle()

    def create_paddle (self):
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.speed("fastest")


    def move_up(self):
        new_y = self.ycor() +MOVING_DISTANCE_Y
        new_x=self.xcor()
        self.goto(x=new_x, y=new_y)

    def move_down(self):
        new_y = self.ycor() - MOVING_DISTANCE_Y
        new_x=self.xcor()
        self.goto(x=new_x, y=new_y)


