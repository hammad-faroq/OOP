from turtle import Turtle
class Scoreborad(Turtle):##INheritence the class with attributs and methods

    def __init__ (self):
        super().__init__()
        self.score=0
        self.hideturtle()
        self.color("white")
        self.penup()
        with open("data.txt") as data:
            self.high_score=int(data.read())
        self.update_score()
    def add_score(self):
        self.score += 1
        self.update_score()

    def reset_score(self):
        if self.score > int(self.high_score):
            pass
            self.high_score = str(self.score)
            with open(file="data.txt",mode="w") as data:
                data.write(self.high_score)
        self.score=0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(0, 270)
        self.write(f"score: {self.score} Highest Score: {self.high_score}", move=False, align='center', font=('courier', 16, 'normal'))

