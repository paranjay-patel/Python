from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.write(f"Score: {self.score}",align="center",font=("Arial",24,"normal"))
        self.hideturtle()

    def increse_score(self):
        self.score += 1
        self.write(f"Score: {self.score}",align="center",font=("Arial",24,"normal"))

    def game_over(self):
        print("game over")
        self.color("blue")
        self.goto(0,0)
        self.write("GAME OVER",align="center",font=("Arial",24,"normal"))