from turtle import Turtle


class Snake:
  def __init__(self):
    self.turtles= []
    self.poisitions=[(-40,0),(-20,0),(0,0)]
    self.creat_snake()
    self.head =  self.turtles[-1]

  
  def creat_snake(self):
    for i in range(len(self.poisitions)):
      new_snake = Turtle()
      new_snake.color('black')
      new_snake.shape('square')
      new_snake.penup()
      new_snake.goto(self.poisitions[i])
      self.turtles.append(new_snake)

  
  def move_snake(self):
    for i in range(len(self.turtles) -1 ):
      self.turtles[i].goto(self.turtles[i + 1].pos())
    self.turtles[-1].forward(21)
    
      
        
  def extend(self):
    new_segment = Turtle()
    new_segment.shape('square')
    new_segment.color('black')
    new_segment.penup()
    self.turtles.insert(0,new_segment)

  
  def up(self):
     self.head.setheading(90)
   
  def down(self):
      self.head.setheading(270)
   
  def right(self):
      self.head.setheading(0)
   
  def left(self):
      self.head.setheading(180)
   


