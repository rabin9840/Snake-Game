#IF WE WANT TO CAPTURE THE FINAL DRAWING CREATED BY THE SNAKE THEN AFTER GAME OVER WE CAN DELETE GAME OVER SIGNAL


from turtle import Turtle
from food import Food

ALIGN="center"
FONT=("Courier",24,"normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.penup()
        self.goto(0,250)
        self.hideturtle()
        self.update_scoreboard()
        self.square=0
        self.triangle=0
        self.circle=0
        
    def update_scoreboard(self):
        self.write(f"Score={self.score}",False,ALIGN,FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",True,ALIGN,FONT)
        self.goto(-30,-30)
        self.write(f"Square={self.square} , Triangle={self.triangle} ,Circle={self.circle}",True,ALIGN,FONT)

        
    def increase_Score(self,food_shape):
        #MODIFICATION
        if food_shape=="square":
            self.score+=4
            self.square+=1
        elif food_shape=="triangle":
            self.score+=3
            self.triangle+=1
        else:
            self.score+=1
            self.circle+=1
            #variable or attribute to count the number of food eaten
            
        self.clear()
        self.update_scoreboard()
        


       
