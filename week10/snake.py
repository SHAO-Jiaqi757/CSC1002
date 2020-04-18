import keyboard
import threading
import random
import time
import curses
from curses import wrapper
help_message = """
Space / Enter   : Pause / Resume
[               : Slower
]               : Faster
H               : Help
Q               : Quit
"""

def push_left():
    if check_update_direction(state['snake'], left):
        state['direction'] = left
    print("Trigger push_left")

def push_right():
    if check_update_direction(state['snake'], right):
        state['direction'] = right
    print("Trigger push_right")

def push_up():
    if check_update_direction(state['snake'], up):
        state['direction'] = up
    print("Trigger push_up")

    
def push_down():
    if check_update_direction(state['snake'], down):
        state['direction'] = down
    print("Trigger push_down")


def faster():
    print("Trigger Faster")
    state['speed'] *= 2
    
def slower():
    print("Trigger Slower")
    state['speed'] /= 2
    
def help_function():
    print("Trigger help")
    
    if state['state'] == 'running':
        state['state'] = 'pause'
    print(help_message)   

def quit_function():
    print("Trigger quit")
    state['state'] = 'quit'
    
def pause_resume():
    print("Trigger Pause Resume")
    if state['state'] == 'running':
        state['state'] = 'pause'
    elif state['state'] == 'pause':
        state['state'] = 'running'

# Static
config = {
    "divider": 50, # The width of divider
    "size-x": 20, # The height of window
    "size-y": 48 # The width of window
}

# Dynamic
state = {
    "state": "running", # "running", "pause", "boundary", "eat_self"
    "time": 0,
    "score": 0,
    "speed": 1, # Speed is the frequency to move.
    "food": [], # A list of 2-element tuple to store the position of the next foods
    "snake": [], # A list of all transition nodes of a snake. The head is at the end of the list!
    "last-direction": (0, 0), # Store the last direction
    "direction": (0, 1), # A 2-element tuple for the snake's direction,
    "blocks": None, # A size-x * size-y tuple of entries
}

# Direction!
up = (-1, 0)
down = (1, 0)
left = (0, -1)
right = (0, 1)

graphic_mapping = {
    None: " ",
    "f": "*",
    "s": "■"
}

def add_2D(x, y):
    
    return (x[0]+y[0], x[1]+y[1])

def check_boundary(pos, x, y):
    """If True, it does not hit the boundary; if False, it hits the boundary."""
    if pos[0] > 0 and pos[0] < x and pos[1] > 0 and pos[1] < y:
        return True
    return False

def check_eat_self(pos, snake):
    """If True, it does not eat itself; if False, it eats itself."""
    if pos in snake:
        return False
    return True

def init_blocks(x, y):
    """Create a x*y 2D array with all None"""
    block = [[None for _ in range(y)] for _ in range(x)]
    return block

def clear_blocks(blocks):
    """Reset the blocks as None"""
    for i in range(len(blocks)):
        for j in range(len(blocks[0])):
            blocks[i][j] = None
    
def update_blocks(blocks, snake, food):
    """
    For position in snake, set the block as 's'
    For position in food, set the block as 'f'
    """
    for (i, j) in snake:
        blocks[i][j] = 's'
    for (i, j) in food:
        blocks[i][j] = 'f'
    

def generate_new_foods(blocks):
    """If there is vacancy, randomly choose one; otherwise, return None"""
    vacancy = [(i,j) for i in range(len(blocks)) for j in range(len(blocks[0])) if blocks[i][j] == None]
    if len(vacancy) == 0:
        return None
        
    return random.choice(vacancy)

def check_update_direction(snake, new_direction):
    """If we can update the direction, return True"""
    if len(snake) == 1:
        return True
    if add_2D(snake[-1], new_direction) == snake[-2]:
        return False

    return True



def init():
    # init blocks
    state['blocks'] = init_blocks(config['size-x'], config['size-y'])
    # generate the first block for snake
    snake_pos = generate_new_foods(state['blocks'])
    state['snake'].append(snake_pos)

    update_blocks(state['blocks'], state['snake'], state['food'])
    
    # generate the first block for food
    food_pos = generate_new_foods(state['blocks'])
    update_blocks(state['blocks'], state['snake'], state['food'])
    
def update_state():
    """
    Check if state["state"] is running, if not, we can return immediately.
    Update state["time"]
    Get the states of all blocks before the move.
    Use the state["direction"] and state["last-direction"] to update the state["food"], state["snake"], and state["blocks"].
    """      
    if state["state"] != "running":
        return
    
    # Update time
    state['time'] += 1
    
    # Clear state["blocks"]
    clear_blocks(state['blocks'])
    
    # Update blocks using snake and food
    update_blocks(state['blocks'], state['snake'], state['food'])
    
    
    # Get the current head and the new head's position
    cur_head = state['snake'][-1]
    new_head = add_2D(cur_head, state['direction'])
    
    # Check if it hits the boundary
    if not check_boundary(new_head, config['size-x'], config['size-y']):
        state['stake'] = 'boundary'
        return

    # Check if it eats itself
    if not check_eat_self(new_head,state['snake']):
        state['state'] = "eat self"
        return
    
    
    # Now the new position is valid, append it to the snake and update blocks
    state['snake'].append(new_head)
    # if snake eats / does not eat food
    if new_head in state['food']:
        state['food'].remove(new_head)
        state['score'] += 1

        update_blocks(state['blocks'], state['snake'], state['food'])
        new_food = generate_new_foods(state['blocks'])

        if new_food is None:  # full of snake
            print("win")
            return
        else:
            state['food'].append(new_food)

    else:
        state['snake'] = state['snake'][1:]

    update_blocks(state['blocks'], state['snake'], state['food'])
    
    return  

def run():
    """The main thread for computation."""
    while True:
        if state["state"] == "running":
            update_state()
            
            draw()
            
            time.sleep(1 / state["speed"])
        elif state["state"] == "pause":
            
            draw()
            
            print(help_message)
            
            time.sleep(1 / state["speed"])
        
        else:
            print("Game over: {}".format(state["state"]))
            print("Your score: {}".format(state["score"]))
            print("Main thread end")
            return
def draw():
    """Draw on screen using state["blocks"] """
    screen.clear()

    screen.addstr("Gluttonous Snake:" + '\n')
    screen.addstr("Time: {} | Score: {} | Speed: {}".format(state["time"], state["score"], state["speed"]) + '\n')
    screen.addstr("-" * config["divider"] + '\n')
    
    # Print your blocks
    for i in range(len(state['blocks'])):
        screen.addstr("|")
        for j in range (len(state['blocks'][i])):
            screen.addstr(graphic_mapping[ state['blocks'][i][j] ])
        screen.addstr("|\n")
    
    screen.addstr("-" * config["divider"] + '\n') ###
    

    screen.refresh()
    return


def main(main_screen = None):

    global screen 
    screen = main_screen

    init()
    main_thread = threading.Thread(target=run)
    # start to run
    main_thread.start()
    # wait for run to stop
    main_thread.join()

    print("Game over...")
    
if __name__ == '__main__':
    keyboard.add_hotkey("up", push_up)
    keyboard.add_hotkey("down", push_down)
    keyboard.add_hotkey("left", push_left)
    keyboard.add_hotkey("right", push_right)
    keyboard.add_hotkey("space", pause_resume)
    keyboard.add_hotkey("enter", pause_resume)
    keyboard.add_hotkey("[", slower)
    keyboard.add_hotkey("]", faster)
    keyboard.add_hotkey("h", help_function)
    keyboard.add_hotkey("q", quit_function)
    # main()
    wrapper(main)