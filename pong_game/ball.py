from math import degrees
from turtle import Turtle
import random
SPEED_BALL = 0


class Ball(Turtle):
    
    degree = random.randint(150,200)

    def __init__(self):
        super().__init__()
        self.penup()
        self.speed(SPEED_BALL)
        self.shape("circle")
        self.shapesize(stretch_len=1,stretch_wid=1)
        self.x_move = 10
        self.y_move = 10
    
    def move_ball(self):
        self.setheading(self.degree)
        self.forward(10)
        print(self.degree)
        
    def change_direction(self):
        if self.xcor()< 0:
            a=random.randint(0,70)
            b=random.randint(300,360)
            self.degree = random.choice([a,b])
        if self.xcor() > 0:
            a=random.randint(120,180)
            b=random.randint(180,240)
            self.degree = random.choice([a,b])
        print(f"balls direction change to {self.degree}")
        
    def wall_collide(self):
        if self.ycor() > 300:
            self.degree = -self.degree
        if self.ycor() < -300:
            self.degree = -self.degree