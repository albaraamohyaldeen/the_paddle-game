from turtle import Screen
from snake import Snake
from food import Food
import time
from scoreboard import Scoreboard


window = Screen()
window.bgcolor('black')
window.setup(800,800)
window.title('_______Snake Game_______')
window.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

game_on =True


while game_on:
  snake.move_snake()
  window.update()
  time.sleep(0.1)
  window.listen()
  window.onkey(snake.up,"Up")
  window.onkey(snake.down,"Down")
  window.onkey(snake.right,"Right")
  window.onkey(snake.left,"Left")
  
  if snake.head.distance(food) < 15:
    snake.extend()
    food.apper()
    score.increase_score()
    
  if snake.head.xcor() > 371 or snake.head.xcor() < -371 : 
      game_on = False
      score.game_over()
    
  elif snake.head.ycor() > 371 or snake.head.ycor() < -371:
      game_on =False
      score.game_over()
      print('')
    
  for segmant in snake.turtles[:-1]:
    if snake.head.distance(segmant) < 10:
      game_on = False
      score.game_over()
      
window.exitonclick()
