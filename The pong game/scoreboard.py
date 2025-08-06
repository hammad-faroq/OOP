from turtle import Turtle

class Scoreboard(Turtle):


    def __init__ (self):

        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_1()
    def update_1 (self):
        self.clear()
        self.goto(-100, 230)
        self.write(f"{self.l_score}", move=False, align="center", font=("courier", 50, "normal"))
        self.goto( 100, 230)
        self.write(f"{self.r_score}", move=False, align="center", font=("courier", 50, "normal"))
    def left_win(self):
        self.l_score += 1
        self.update_1()

    def right_win(self):
        self.r_score  += 1
        self.update_1()

