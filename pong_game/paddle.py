from turtle import Turtle 
import random
import turtle
from ball import Ball

class Paddle(Turtle):
    
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_len=1,stretch_wid=6)

    def up(self):
        y = self.ycor()
        y += 30
        self.goto(-470,y)
    
    def down(self):
        y = self.ycor()
        y -= 30
        self.goto(-470,y)
           