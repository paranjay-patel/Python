
import random
from secrets import choice
import turtle as t

pal = t.Turtle()
t.colormode(255)
pal.width(10)
pal.hideturtle()
pal.speed(20)
colors=['slate blue','lime','orange red','purple','gold','indigo','cyan','hot pink']
angles = [90,180,270,360]

while True:
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    pal.color(r,g,b)
    pal.forward(30)
    pal.right(random.choice(angles))
    
  
