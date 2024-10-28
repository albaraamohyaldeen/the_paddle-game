from turtle import Turtle

class Scoreboard(Turtle):
  def __init__(self):
    super().__init__()
    self.score = 0
    self.color('white')
    self.penup()
    self.goto(0,350)
    self.update_score()
    
  def update_score(self):
    self.write(f'Score is: {self.score}', align= 'center',font=('Arial',25,'normal'))
    
  def increase_score(self):
    self.score += 1
    self.clear()
    self.update_score()

  def game_over(self):
    self.screen.bgcolor('darkred')
    self.goto(0,0)
    self.write(f'Game Over\nScore:{self.score}',align='center',font=('Arial',25,'normal'
    ))
