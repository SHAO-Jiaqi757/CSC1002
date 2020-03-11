def introduction():
    print("sliding puzzle game for both 8 and 15 numbers. \
        For an 8-number puzzle, it has a square-framed board consisting of 8 square tiles, numbered 1 to 8, initially placed in random order, \
            while a 15-number puzzle there are 15 numbered square tiles, from 1 to 15.\
                The board has an empty space where an adjacent tile can be slid to. \
                    The objective of the game is to re-arrange the tiles into a sequential order by their numbers (left to right, top to bottom) by repeatedly making sliding moves (left, right, up or down).")

def print_8_puzzle(out):    
    row = 1
    while row <= 3:
        
        col = 1
        while col <= 3:
            num = out[row-1][col-1]
            if num == 0:  # find the position of 0
                pos_0_row= row
                pos_0_col = col
            print(num, end="")
            
            col += 1
        print()
        row += 1

        

        

# def function allowing to move to left, right, up and down
def move_lrud(out, l, r, u, d):  
    get_move = input("Enter your move (left-%s, right-%s, up-%s, down-%s) > " % (l, r, u, d))
    if get_move == l:  # change the positon 
        out[1][0], out[1][1] = out[1][1], out[1][0]

    elif get_move == r:
        out[1][2], out[1][1] = out[1][1], out[1][2]

    elif get_move == u:
        out[0][1], out[1][1] = out[1][1], out[0][1]

    elif get_move == d:
        out[2][1], out[1][1] = out[1][1], out[2][1]
    
    else:
        print("invaild input!!")
    
    


def choose():  # choose 8 or 15 puzzles
    pass


def ifSolvable():  # 
    pass