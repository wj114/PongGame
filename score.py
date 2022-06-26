from turtle import Turtle

Alignment = "center"
Font = ("Arial", 80, "normal")


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.left_score = 0
        self.right_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.goto(-100, 200)
        self.write(self.left_score, False, align=Alignment, font=Font)
        self.goto(100, 200)
        self.write(self.right_score, False, align=Alignment, font=Font)

    def left_paddle_score(self):
        self.left_score += 1
        self.clear()
        self.update_score()

    def right_paddle_score(self):
        self.right_score += 1
        self.clear()
        self.update_score()
