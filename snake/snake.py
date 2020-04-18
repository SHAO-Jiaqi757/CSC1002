from turtle import Turtle
from outline import *
w = Screen()
snake = create_turtle("square", color=("yellow", "blue"))
snake.stamp()
snake.forward(20)
snake.stamp()
snake.forward(20)
snake.clearstamps(1)
w.mainloop()
