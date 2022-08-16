from turtle import Turtle, Screen

pal=Turtle()
screen = Screen()

def move_forwards():
    pal.forward(10)

def move_backwards():
    pal.backward(10)

def move_left():
    pal.left(10)

def move_right():
    pal.right(10)

def clear():
    pal.clear()
    pal.penup()
    pal.home()
    pal.pendown()

screen.listen()
screen.onkey(move_forwards,"w")
screen.onkey(move_backwards,"s")
screen.onkey(move_left,"a")
screen.onkey(move_right,"d")
screen.onkey(clear,"c")

screen.exitonclick()