from turtle import Turtle
LIST=[(0,0),(-20,0),(-40,0)]
# MOVE_DISTANT=20
class Snake:
    def __init__ (self):
        self.segment= []
        self.create_snake()
        self.head=self.segment[0]
    def create_snake(self):
        for position in LIST:
            self.add_new(position)


    def add_new(self,position):
        new = Turtle()
        new.shape("square")
        new.penup()
        new.color("white")
        new.goto(position)
        self.segment.append(new)
    def extend(self):
        self.add_new(self.segment[-1].position())
        
    def reset(self):
        for seg in self.segment:
            seg.goto(1000,1000)
        self.segment.clear()
        self.create_snake()
        self.head=self.segment[0]


    def move(self):
        for number in range(len(self.segment)-1, 0, -1):
            nx=self.segment[number-1].xcor()
            ny=self.segment[number-1].ycor()
            self.segment[number].goto(x=nx, y=ny)
        self.segment[0].forward(20)

    def up(self):
        if self.segment[0].heading() !=270:
            self.segment[0].setheading(90)

    def down(self):
        if self.head.heading() !=90:
            self.segment[0].setheading(270)

    def right(self):
        if self.segment[0].heading() !=180:
            self.segment[0].setheading(0)

    def left(self):
        if self.segment[0].heading() !=0:
            self.segment[0].setheading(180)
