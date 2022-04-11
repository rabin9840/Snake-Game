from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        #color value for different color of food created in the screen
        super().__init__()
        #now we can modify the turtle attributes and methods as the 
        #method and attribute of the food class
        self.shape("square")
        self.color("red")
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)

    def refresh(self):
        random_x=random.randint(-280,280)
        random_y=random.randint(-280,280)
        #here we are using or updating the goto method from turtle class
        self.goto(random_x,random_y)
    
    