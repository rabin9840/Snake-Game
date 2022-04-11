from turtle import Turtle,Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen=Screen()

#for setting the screen background color black
screen.bgcolor("black")

#for setting the size of the screen
screen.setup(width=600,height=600)

#for setting the title of the screen
screen.title("My Snake Game")
screen.tracer(0)

snake=Snake()
food=Food()
scoreboard=Scoreboard()

#to control the direction of the snake movement
screen.listen()

screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

#game running or executing code
is_game_on=True

while is_game_on:
    screen.update()
    time.sleep(0.1)
    
    snake.move()

    #To detect collision with food
    if snake.head.distance(food)<10:
        food.refresh()
        snake.extend()
        scoreboard.increase_Score()
    
    #TO DETECT COLLISION WITH THE WALL
    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()<-280 or snake.head.ycor()>280:
        is_game_on=False
        scoreboard.game_over()

    #DETECT THE COLLISION BETWEEN THE SEGMENTS OF THE BODY OF SNAKE
    for segments in snake.segments:
        if segments==snake.head:
            pass
        elif snake.head.distance(segments)<5:
            is_game_on=False
            scoreboard.game_over()





#for exiting the screen when clicking it
screen.exitonclick()
