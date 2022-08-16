import turtle as t
import random
pal = t.Turtle()
pal.speed("fastest")
colors=['slate blue','orange red','purple','gold','indigo','cyan','hot pink']
while True:
    color = random.choice(colors)
    pal.circle(100)
    pal.left(5)
    pal.color(color)
    if pal.heading() == 0.0:
        break

screen = t.Screen()
screen.exitonclick()
