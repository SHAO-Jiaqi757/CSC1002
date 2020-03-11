def introduction():
    print("=" * 80)
    print("<<< Introdution >>>")
    print("-"*80)
    print("Sliding Puzzle Game for both 8 and 15 numbers.\n \
For an 8-number puzzle, it has a square-framed board consisting of 8 square tiles, numbered 1 to 8, initially placed in random order, \n \
While a 15-number puzzle there are 15 numbered square tiles, from 1 to 15.\n \
The board has an empty space where an adjacent tile can be slid to. \n \
The objective of the game is to re-arrange the tiles into a sequential order by their numbers (left to right, top to bottom) by repeatedly making sliding moves (left, right, up or down).")
    print("-" * 80)


def direction_letters():
    while True:
        try:
            l,r,u,d = input("Enter the four letters used for left, right, up and down directions >").split()
            return l,r,u,d
            break
        except:
            print("Please enter four letters")
            continue


def move(out,u,d,r,l,pos_0_row,pos_0_col,*arg):
    
    while True:
        try:
            result = input("Enter your move {} >".format(tuple(arg)))
            if result == u:
                out[pos_0_row+1][pos_0_col], out[pos_0_row][pos_0_col] = out[pos_0_row][pos_0_col], out[pos_0_row+1][pos_0_col]
                break
            elif (result == d) and (pos_0_row-1>=0):
                out[pos_0_row-1][pos_0_col], out[pos_0_row][pos_0_col] = out[pos_0_row][pos_0_col], out[pos_0_row-1][pos_0_col]
                break
            elif (result == r) and (pos_0_col-1>=0) :
                out[pos_0_row][pos_0_col-1], out[pos_0_row][pos_0_col] = out[pos_0_row][pos_0_col], out[pos_0_row][pos_0_col-1]
                break
            elif result == l:
                out[pos_0_row][pos_0_col+1], out[pos_0_row][pos_0_col] = out[pos_0_row][pos_0_col], out[pos_0_row][pos_0_col+1]
                break
            else:
                print("Please follow the instruction to enter!! Please enter a letter again!")
                continue
        except:
            print("Please follow the instruction to enter!!")
            continue


def isSolvable_8(*arg):
    sum = 0
    for i in range(len(arg)):
        if arg[i] == 0:
            pass
        else:
            for j in range(0, i):
                if arg[j] > arg[i]:
                    sum += 1    
    if sum % 2 == 0:
        return True
    else:
        return False


def isSolvable_15(*arg):
    sum = 0
    for i in range(len(arg)):
        if arg[i] == 0:
            indx_0 = i
        else:
            for j in range(0, i):
                if arg[j] > arg[i]:
                    sum += 1   

    row_0 = indx_0 % 3 
    if (sum % 2 == 0) and ((3-row_0)%2 == 0):
        return True
    elif (sum % 2 != 0) and ((3-row_0)%2 != 0):
        return True
    else:
        return False


def isSuccess_8(out,count):
    # break if 8 puzzles in sequence    
    match = 0
    for row in range(3):
        for col in range(3):
            if (out[row][col] != row * 3 + (col + 1)) and (out[2][2] != " "):
                return
            elif out[row][col] == row * 3 + (col + 1):
                match += 1
    if out[2][2] == " ":
        match += 1
    if match == 9:
        print("Congratulations! You solved the puzzle in %d moves!" %count)
        return True


def isSuccess_15(out,count):
    # break if 8 puzzles in sequence    
    match = 0
    for row in range(4):
        for col in range(4):
            if (out[row][col] != row * 4 + (col + 1)) and (out[3][3] != " "):
                return
            elif out[row][col] == row * 4 + (col + 1):
                match += 1
    if out[3][3] == " ":
        match += 1
    if match == 16:
        print("Congratulations! You solved the puzzle in %d moves!" %count)
        return True
