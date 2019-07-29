import turtle
import random

turtle.tracer(1,0)

SIZE_X = 800
SIZE_Y = 500
turtle.setup(SIZE_X, SIZE_Y)

turtle.penup()

SQUARE_SIZE = 20
START_LENGTH = 6
TIME_STEP = 100

pos_list = []
stamp_list = []
food_stamps = []
food_pos = []

snake = turtle.clone()
snake.shape("square")

turtle.hideturtle()

def new_stamp():
    snake_pos = snake.pos()

    pos_list.append(snake_pos)      
    new_stamp= snake.stamp()    
    stamp_list.append(new_stamp)

for counter in range(START_LENGTH):
        snake_x,snake_y=snake.pos()
        snake.goto(snake_x +SQUARE_SIZE, snake_y) #Move snake to new (x,y)

        new_stamp()
    
   
#turtle.mainloop()
