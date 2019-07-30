import turtle
import random

turtle.tracer(1,0)

SIZE_X = 800
SIZE_Y = 500
turtle.setup(SIZE_X, SIZE_Y)

turtle.penup()

SQUARE_SIZE = 20
START_LENGTH = 5
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
    
def remove_tail():
    old_stamp = stamp_list.pop(0) # last piece of tail
    snake.clearstamp(old_stamp) # erase last piece of tail
    pos_list.pop(0) # remove last piece of tail's position

snake.direction = "Up"
TOP_EDGE = 250
BOTTOM_EDGE = -250
RIGHT_EDGE = 400
LEFT_EDGE = -400

def up():
    snake.direction="Up" 
    print("You pressed the up key!")

snake.direction = "Down"

def down():
    snake.direction="Down"
    print("You pressed the down key")

snake.direction = "Left"

def left():
    snake.direction="Left"
    print("You pressed the left key")

snake.directon = "Right"

def right():
    snake.direction="Right"
    print("You pressed the right key")

turtle.onkeypress(up, "Up") 
turtle.onkeypress(down, "Down") 
turtle.onkeypress(left, "Left") 
turtle.onkeypress(right, "Right")

turtle.listen()

turtle.register_shape("trash.gif")

food = turtle.clone()
food.shape("trash.gif")
food_pos = [(100,100), (-100,100), (-100,-100), (100,-100)]
food_stamps = []

for this_food_pos in food_pos:
    food.goto(this_food_pos)
    food_stamps.append(food.stamp())

def move_snake():
    my_pos = snake.pos()
    x_pos = my_pos[0]
    y_pos = my_pos[1]

    if snake.direction == "Up":

        snake.goto(x_pos, y_pos + SQUARE_SIZE)
        print("You moved up!")
    elif snake.direction=="Down":
        snake.goto(x_pos, y_pos - SQUARE_SIZE)
        print("You moved down!")
    elif snake.direction == "Right":
        snake.goto(x_pos + SQUARE_SIZE, y_pos)
        print("You moved right!")
    elif snake.direction == "Left":
        snake.goto(x_pos - SQUARE_SIZE, y_pos)
        print("You moved left!")

    new_pos = snake.pos()
    new_x_pos = new_pos[0]
    new_y_pos = new_pos[1]


    if new_x_pos >= RIGHT_EDGE:
         print("You hit the right edge! Game over!")
         quit()
    if new_x_pos <= LEFT_EDGE:
         print("You hit the left edge! Game over!")
         quit()
    if new_y_pos >= TOP_EDGE:
         print("You hit the top edge! Game over!")
         quit()
    if new_y_pos <= BOTTOM_EDGE:
         print("You hit the bottom edge! Game over!")
         quit()
    new_stamp()

    ######## SPECIAL PLACE - Remember it for Part 5

    if snake.pos() in food_pos:
        food_index=food_pos.index(snake.pos()) 
        food.clearstamp(food_stamps[food_index]) 
        food_pos.pop(food_index) 
        food_stamps.pop(food_index) 
        print("You have eaten the food!")

    turtle.ontimer(move_snake,TIME_STEP)

    remove_tail()
move_snake()
turtle.mainloop()
