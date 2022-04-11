from turtle import Turtle

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
        
    def update_scoreboard(self):
        self.write(f"Score={self.score}",False,ALIGN,FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",True,ALIGN,FONT)

        
    def increase_Score(self):
        self.score+=1
        self.clear()
        self.update_scoreboard()
        
       
