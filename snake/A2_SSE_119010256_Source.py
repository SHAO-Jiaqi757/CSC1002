from turtle import Turtle, Screen
from functools import partial
import random
key_pressed = None
snake_len = 5  # Original length
snake_speed_timer = 220
state = "stop"  # Run, pause, hit boundary, eat food, game over, win
f_pos = {}  # Store the key ->position(x, y), value ->(food_i, i)
food = {}  # Store food Turtles
snake_body = []  # Store the position of body(stamps).
time = 0
body_contact = 0


def create_screen():
    screen = Screen()
    screen.setup(500, 500)  # 500 x 500
    screen.title("Snake")
    screen.tracer(0)  # Turn off auto refresh.
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


def write(tt, txt, x, y, ft="normal"):
    tt.hideturtle()
    tt.up()
    tt.goto(x, y)
    tt.down()
    tt.write(txt, font=("Arial", 15, ft))


def set_food():
    global f_pos, food
    # Create 9 turtles(food).
    for i in range(1, 10):
        obj = "food" + str(i)
        food[obj] = Turtle()
        x = random.randint(-235, 235)
        y = random.randint(-235, 235)
        write(food[obj], str(i), x, y)
        f_pos[(x, y)] = (obj, str(i))


def eat_food():
    global snake_len, state, snake_speed_timer
    snake_x, snake_y = snake.position()
    for (x, y) in f_pos.keys():
        # Visible food number have positional error with food pos(x, y)
        if abs(snake_x-(x+2)) < SIDE_LEN/2 and abs(snake_y-(y)) < SIDE_LEN/2:
            food_turtle_str, food_num = f_pos[(x, y)]
            food[food_turtle_str].clear()  # Clear the food
            snake_len += int(food_num)
            x_eat, y_eat = x, y
            state = "eat_food"
            snake_speed_timer += 6
    if state == "eat_food":
        f_pos.pop((x_eat, y_eat))
        food.pop(food_turtle_str)  # Remove the consumed food.
        if food == {}:
            state = "win"
            return
    state = "run"
    w.update()


def on_key_unpause():  # Unpause when the second "space" was pressed.
    global state
    state = "run"
    w.onkey(on_key_pause, "space")
    begin_game()
    w.listen()


def on_key_pause():  # Press "space" to pause.
    global state
    state = "pause"
    w.onkey(None, "space")  # Unbind "space" and pause function.
    w.onkey(on_key_unpause, "space")


def on_click(x, y):
    global state
    game_status.undo()
    set_food()
    w.update()
    begin_game()
    w.onclick(None)  # End click events


def title():  # Set title
    global time
    if (state != "game_over") and (state != "win"):
        time += 1
        w.title("Snake: contact : {} ;time: {}s".format(body_contact, time))
        w.update()
        w.ontimer(title, 1000)


def begin_game():
    global state
    state = "run"  # Change the state to run
    w.ontimer(title, 1000)
    w.ontimer(monster_move, random.randint(240, 700))
    get_key()
    w.ontimer(move_snake, snake_speed_timer)
    w.listen()


def collapse(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2
    if abs(x1 - x2) <= SIDE_LEN and abs(y1 - y2) <= SIDE_LEN:
        return True
    return False


def game_over():
    global state
    if collapse(monster.position(), snake.position()):
        state = "game_over"


def monster_pos():
    while True:
        x = random.randint(-250, 250)
        y = random.randint(-250, 250)
        if snake.distance(x, y) >= 100:
            return x, y


def monster_move():
    global state, body_contact
    if (state == "run") or (state == "pause"):
        x_m, y_m = monster.position()
        x_s, y_s = snake.position()
        d_x = abs(x_s-x_m)
        d_y = abs(y_s-y_m)
        if d_x >= d_y:
            if x_s > x_m:  # Snake is in the right
                heading = 0
            elif x_s < x_m:
                heading = 180   # Snake is in the left
        elif d_x < d_y:
            if y_s > y_m:
                heading = 90  # Snake is above
            elif y_s < y_m:
                heading = 270  # Snake is below

        monster.setheading(heading)
        monster.up()
        monster.forward(SIDE_LEN)
        monster.down()

        for b_pos in snake_body:
            if collapse(monster.position(), b_pos):
                body_contact += 1
                break
        game_over()
        w.update()
        w.ontimer(monster_move, random.randint(240, 700))


def move_up():
    global snake_len
    extend_snake(snake_len, heading=90)


def move_down():
    global snake_len
    extend_snake(snake_len, heading=270)


def move_right():
    global snake_len
    extend_snake(snake_len, heading=0)


def move_left():
    global snake_len
    extend_snake(snake_len, heading=180)


def hit_boundary():
    global state, key_pressed
    _x, _y = snake.position()
    if not (not ((_x <= -250 + SIDE_LEN / 2) and (key_pressed == "Left"))
            and not (
            (_x >= 250 - SIDE_LEN / 2) and (key_pressed == "Right"))) \
            or ((_y <= -250 + SIDE_LEN/2) and (key_pressed == "Down"))\
            or ((_y >= 250 - SIDE_LEN/2) and (key_pressed == "Up")):
        state = "hit_boundary"
        key_pressed = None


def move_snake():
    global state, key_pressed
    if state == "run":
        w.onkey(on_key_pause, "space")
        if key_pressed == "Up":
            move_up()
        elif key_pressed == "Down":
            move_down()
        elif key_pressed == "Right":
            move_right()
        elif key_pressed == "Left":
            move_left()
        hit_boundary()  # If the snake hit boundary, state change
        eat_food()
        w.ontimer(move_snake, snake_speed_timer)
    elif state == "game_over":
        game_status.pencolor("orange")
        write(game_status, "Game Over!!!", *snake.position(), ft="bold")
    elif state == "win":
        game_status.pencolor("orange")
        write(game_status, "WIN!!!", *snake.position(), ft="bold")
    elif state == "hit_boundary":
        get_key()  # Get new key
        state = "run"  # Let the snake move again


def current_key_pressed(key):
    """
    Change key_pressed when next key is pressed
    """
    global key_pressed
    key_pressed = key


def get_key():
    w.onkey(partial(current_key_pressed, "Up"), "Up")
    w.onkey(partial(current_key_pressed, "Down"), "Down")
    w.onkey(partial(current_key_pressed, "Left"), "Left")
    w.onkey(partial(current_key_pressed, "Right"), "Right")
    w.update()


def clean_extend():  # Clear stamps like queue to move snake
    global state, snake_body
    if state == "run" and len(snake.stampItems) > snake_len:
        snake.clearstamps(1)
        snake_body = snake_body[1:]
        w.update()


def extend_snake(length=5, heading=0):  # Extend the body of snake
    global snake_speed_timer
    if 5 < len(snake_body) < length:
        snake_speed_timer += 6  # Slower the snake as the body extending.
    color = snake.color()  # Get the color of head
    snake.color('black', 'purple')  # Set the color of body
    x, y = snake.position()
    snake.up()
    snake.stamp()
    snake.setheading(heading)  # Change the heading
    snake.forward(SIDE_LEN)
    snake.down()
    snake_body.append((int(x), int(y)))
    snake.color(*color)  # Restore the color of head
    w.ontimer(clean_extend, snake_speed_timer)
    w.update()


if __name__ == "__main__":
    w = create_screen()
    snake = create_turtle("square", ("purple", "red"))
    x, y = monster_pos()
    monster = create_turtle("square", ("black", "green"), x, y)
    w.update()
    SIDE_LEN = get_side_len()
    game_status = Turtle()
    write(game_status, 'Welcome !!! \n '
                       '\nYou can use 4 raw keys to control the snake\n'
                       'Eat all food and be careful of monster!!\n '
                       '\nClick anywhere on the screen to start your game !!',
          -180, 120)
    w.onclick(on_click)  # Begin the game
    w.mainloop()
