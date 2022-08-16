from turtle import Turtle,Screen, ycor
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
player = Paddle()
opponent = Paddle()
ball = Ball()
score_p = Scoreboard(-100)
score_o = Scoreboard(100)

screen.setup(width=1000 , height=600)
player.goto(-470,0)
opponent.goto(470,0)

screen.listen()
screen.onkeypress(player.up,"Up")       
screen.onkeypress(player.down,"Down")

is_game_on = True
y=0
while is_game_on:
    ball.move_ball()
    if ball.distance(player) < 60 and ball.xcor() < -460:
        ball.change_direction()
        print("*******************  collision with player  *****************8")
    #print(ball.heading())
    if ball.distance(opponent) < 60 and ball.xcor() > 460:
        ball.change_direction()
        print("*******************  collision with opponent  *****************8")
    if ball.ycor() > 300 or ball.ycor() < -300:
        ball.wall_collide()
        print("****** collide with wall *******")
    if ball.xcor() > 500 :
        score_p.increse_score()
        ball.goto(0,0)
        print("****** gose out of screen *******")
    if ball.xcor() < -500:
        score_o.increse_score()
        ball.goto(0,0)
        print("****** gose out of screen *******")   
   
    if abs(ball.ycor() - opponent.ycor()) > 25:
        if ball.ycor() > opponent.ycor():
            y= y+5
            opponent.goto(470,y) 
        if ball.ycor() < opponent.ycor() :
            y=y-5
            opponent.goto(470,y) 













screen.exitonclick()
