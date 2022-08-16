from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self,xcor):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(xcor,250)
        self.write(f"Score: {self.score}",align="center",font=("Arial",24,"normal"))
        self.hideturtle()

    def increse_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}",align="center",font=("Arial",24,"normal"))

    def game_over(self):
        self.goto(0,0)
        self.clear()
        self.write("GAME OVER",align="center",font=("Arial",24,"normal"))