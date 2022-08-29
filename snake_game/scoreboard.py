from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        with open("snake_game\data.txt",mode="r") as file:
            high_score = file.read()
            print(f"high_score type : {type(high_score)}")
        self.score = 0
        self.highest_score = high_score
        self.color("white")
        self.penup()
        self.goto(0,250)
        self.hideturtle()
        self.write(f"Score: {self.score}  highest: {self.highest_score}",align="center",font=("Arial",24,"normal"))

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}  highest: {self.highest_score}",align="center",font=("Arial",24,"normal"))

    def increse_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > int(self.highest_score):
            self.highest_score = self.score
        with open("snake_game\data.txt",mode="w") as file:
            file.write(str(self.highest_score))
        self.score = 0
        self.update_scoreboard()   
    
    # def game_over(self):
    #     print("game over")
    #     self.color("blue")
    #     self.goto(0,0)
    #     self.write("GAME OVER",align="center",font=("Arial",24,"normal"))