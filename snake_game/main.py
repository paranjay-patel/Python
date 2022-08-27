from pickle import FALSE
import time
from turtle import Turtle,Screen
from food import Food
from snake import Snake
from scoreboard import Scoreboard
screen = Screen()
screen.setup(width=600 , height=600)
screen.bgcolor("black")
screen.title("snake game")
screen.tracer(0)

# turtle = Turtle()
snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")       
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on = True


while game_is_on:

    screen.update()
    time.sleep(0.1)
    snake.move()
    
    #detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.clear()
        snake.extend()
        scoreboard.increse_score()
  
    #detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on= False
        print("collide with wall")
        scoreboard.game_over()

    #detect collision with tail
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()
            print("collide")
    #if head collides with any segment in the tail

screen.exitonclick()