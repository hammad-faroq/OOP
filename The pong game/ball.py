from turtle import Turtle
class Ball(Turtle):


    def __init__ (self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.speed(1)
        self.shapesize(stretch_wid=1,stretch_len=1)
        self.new_x=10
        self.new_y=10
        self.move_speed =0.07

    def move_up(self):
        self.just_move()
    def move_oppostie(self):
        self.new_x *= -1
        self.just_move()
        self.move_speed =0.07
    def just_move(self):
        new_x = self.xcor() + self.new_x
        new_y = self.ycor() + self.new_y
        self.goto(new_x, new_y)
    def again(self):
        self.new_x=10
        self.new_y=10
        self.move_speed =0.07
        self.just_move()
    def bounce_y(self):
        self.new_y *= -1
        self.move_speed *=0.9

    def bounce_x(self):
        self.new_x *=-1
        self.move_speed *= 0.9