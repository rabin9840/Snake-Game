from turtle import Turtle,Screen
import time
from snake_modification import Snake
from food_modification import Food
from scoreboard_modification import Scoreboard
import random

#MDOIFICATION
color=["red","blue","green","violet","yellow"]
shapes=["square","triangle","circle"]

all_foods=[]

screen=Screen()

#for setting the screen background color black
screen.bgcolor("black")

#for setting the size of the screen
screen.setup(width=600,height=600)

#for setting the title of the screen
screen.title("My Snake Game")
screen.tracer(0)

snake=Snake()


#MODIFICAITON NUMBER 1
#HERE WE ARE MAKING MULTILE FOOD OF DIFFERENT RANDOM COLOR
for foods in range(0,5):
    food=Food(random.choice(color),random.choice(shapes))
    food.goto(random.randint(-280,280),random.randint(-280,280))
    all_foods.append(food)

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
    #here we are checking the snake speed for updating screen speed
    time.sleep(snake.move_speed)
    screen.update()
    snake.move()
    

        #MODIFICATION
    #TO INCREASE THE SPEED OF THE SNAKE AFTER CERTAIN SCORE

    #if scoreboard.score<5:
    #    pass
    #elif scoreboard.score<10:
    #    snake.increase_speed(0.05)
    #else:
    #    snake.increase_speed(0.07)
    #
   

    #To detect collision with food
    
    #MODIFICATION NO2
    #here we are updating the score and food location for all food objects
    for food in all_foods:
        if snake.head.distance(food)<10:
            food.refresh()
            snake.extend()
            scoreboard.increase_Score(food.shape())
    

    
    #TO DETECT COLLISION WITH THE WALL
    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()<-280 or snake.head.ycor()>280:
        is_game_on=False
        scoreboard.game_over()

    #DETECT THE COLLISION BETWEEN THE SEGMENTS OF THE BODY OF SNAKE

    for segments in snake.segments[1:]:
    #here we are using slicing where we arenot checking the head of the snake
        if snake.head.distance(segments)<5:
            is_game_on=False
            scoreboard.game_over()





#for exiting the screen when clicking it
screen.exitonclick()
