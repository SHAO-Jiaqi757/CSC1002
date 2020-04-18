from turtle import Turtle, Screen
from functools import partial
import random

key_pressed = None
monster_move_choice = {"quadrant_1": [90, 0],  # ("up", "right")
                       "quadrant_2": [90, 180],  # ("up", "left")
                       "quadrant_3": [270, 180],  # ("down", "left")
                       "quadrant_4": [270, 0]}  # ("down", "right")
state = "stop"  # Run, Pause, game over, win
snake_id = []

def create_screen():
    screen = Screen()
    screen.setup(500, 500)  # 500 x 500
    screen.title("Snake")
    screen.tracer(0)
    return screen


def get_side_len():  # Get the length of square shape
    vertex = snake.get_shapepoly()
    x0, y0 = vertex[0]
    for i in range(1, len(vertex)):
        xi, yi = vertex[i]
        if x0 == xi:
            side_len = abs(y0 - yi)
            break
    return side_len


def create_turtle(shape, color, x=0, y=0):  # Create a snake or a monster
    tt = Turtle()
    tt.up()
    tt.goto(x, y)
    tt.down()
    tt.shape(shape)
    tt.color(*color)
    return tt


def write(tt, txt, x, y):
    tt.hideturtle()
    tt.up()
    tt.goto(x, y)
    tt.down()
    tt.write(txt, font=20)


def set_food():
    food = Turtle()
    food.speed(0)
    for i in range(1, 10):
        x = random.randint(-250, 250)
        y = random.randint(-250, 250)
        write(food, str(i), x, y)
    w.update()
    return food


def on_click(x, y):
    global state
    info.undo()
    state = "run"
    w.update()
    begin_game()


def begin_game():
    if state == "run":
        food = set_food()
        monster_move()
        get_key()
        w.ontimer(move_snake, 500)
        w.listen()


def monster_pos():
    while True:
        x = random.randint(-250, 250)
        y = random.randint(-250, 250)
        if snake.distance(x, y) >= 100:
            return x, y


def monster_move_direction(direct):  # Up / down / right / left
    monster.setheading(direct)
    monster.up()
    monster.forward(SIDE_LEN)
    monster.down()


def monster_move():
    angle = monster.towards(*snake.position())
    if 0 < angle < 90:  # Up or right
        heading = random.choice(monster_move_choice["quadrant_1"])
    elif 90 < angle < 180:  # Left or up
        heading = random.choice(monster_move_choice["quadrant_2"])
    elif 180 < angle < 270:  # Down or left
        heading = random.choice(monster_move_choice["quadrant_3"])
    elif 270 < angle < 360:  # Right or down
        heading = random.choice(monster_move_choice["quadrant_4"])
    else:  # 0, 90, 180, 270
        heading = angle

    monster_move_direction(heading)
    w.update()
    w.ontimer(monster_move, 500)


def move_up():
    extend_snake(heading=90)


def move_down():
    extend_snake(heading=270)


def move_right():
    extend_snake(heading=0)


def move_left():
    extend_snake(heading=180)


def move_snake():
    if key_pressed == "Up":
        move_up()
    elif key_pressed == "Down":
        move_down()
    elif key_pressed == "Right":
        move_right()
    elif key_pressed == "Left":
        move_left()
    w.ontimer(move_snake, 500)


def current_key_pressed(key):  # Change key_pressed when next key is pressed
    global key_pressed
    key_pressed = key


def get_key():
    w.onkey(partial(current_key_pressed, "Up"), "Up")
    w.onkey(partial(current_key_pressed, "Down"), "Down")
    w.onkey(partial(current_key_pressed, "Left"), "Left")
    w.onkey(partial(current_key_pressed, "Right"), "Right")
    w.update()


def clean_extend(length=5):
    global snake_id
    snake.clearstamps(1)
    snake_id = snake_id[1:]
    w.ontimer(clean_extend, 500)


def extend_snake(length=5, heading=0):  # Extend the body of snake
    global snake_id
    color = snake.color()  # Get the color of head
    snake.color('black', 'purple')  # Set the color of body
    snake.up()
    snake.stamp()
    snake_id.append(snake.stamp())
    snake.setheading(heading)  # Change the heading
    snake.forward(SIDE_LEN)
    snake.down()
    snake.color(*color)  # Restore the color of head
    print(snake_id)
    if len(snake_id) == length:
        w.ontimer(clean_extend, 500)

    w.update()


if __name__ == "__main__":
    w = create_screen()
    snake = create_turtle("square", ("purple", "red"))
    x, y = monster_pos()
    monster = create_turtle("square", ("black", "green"), x, y)
    SIDE_LEN = get_side_len()

    info = Turtle()
    write(info, 'Welcome !!! \n You can use 4 raw keys to control the snake\n'
                'Eat all food and be careful of monster!!\n '
                'Click anywhere on the screen to start your game !!',
                -150, 150)
    w.onclick(on_click)  # Clear the information

    w.mainloop()
