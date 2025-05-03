from turtle import Turtle


class ScoreBord(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.up()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.updatescore()

    def updatescore(self):
        self.clear()
        self.goto(-100, 230)
        self.write(self.l_score, align="center", font=("courier", 80, "normal"))
        self.goto(100, 230)
        self.write(self.r_score, align="center", font=("courier", 80, "normal"))

    def leftscore(self):
        self.l_score += 1

    def rightscore(self):
        self.r_score += 1
