from turtle import Turtle

#CONSTANT TO HOLD THE POSITION OF THE SNAKE
STARTING_POSITION=[(0,0),(-20,0),(-40,0)]

UP=90
DOWN=270
LEFT=180
RIGHT=0

class Snake(Turtle):
    def __init__(self):
        super().__init__()
        self.segments=[]
        #to hold the segment of the snake body part
        self.create_snake()
        #HERE WE ARE ASSIGNING THE SEGMENT[0] AS THE HEAD OF THE SNAKE
        self.head=self.segments[0]
        self.move_speed=0.1
  

    def add_segment(self,position):
        new_segment=Turtle("square") #here square is the shape of the snake or turtle object
        new_segment.color("white")
        new_segment.penup()
            #now to set up the position of the square snake
        new_segment.goto(position)
        self.segments.append(new_segment)
            #here we need to use self. in append because we are using segment inside class
        

    def extend(self):
        #add a new segment to the body of the snake
        self.add_segment(self.segments[-1].position())

    def create_snake(self):
        ''' To create the snake body'''
        for position in STARTING_POSITION:
            self.add_segment(position)
           
            
            

    def move(self):
        for seg_num in range(len(self.segments)-1,0,-1):
            #this code only includes other part of the snake except 0 i.e. all_snake[0]
            new_x=self.segments[seg_num-1].xcor()
            #for 1st iteration 2
            #new_x=all_snake[2-1=1].xcor
            new_y=self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(new_x,new_y)
       # self.segments[0].forward(20)
        self.head.fd(10)
    
    #def increase_speed(self,increase):
    #    self.move_speed+=increase

    def up(self):
        if self.head.heading()!=270:
            self.head.setheading(90)

    def down(self):
        if self.segments[0].heading()!=90:
            self.head.setheading(270)
    
    def left(self):
        if self.head.heading()!=0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading()!=180:
            self.head.setheading(0)




