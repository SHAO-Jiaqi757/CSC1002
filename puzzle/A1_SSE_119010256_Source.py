from random import shuffle


def direction_letters():
    while True:
        received_letters = list(
            input("Enter the four letters used for left, right, up and down directions > "))

        for letter in received_letters:
            if not letter.isalpha():
                received_letters.remove(letter)

        if len(received_letters) != 4:
            continue

        if len(received_letters) != len(set(received_letters)):
            print("Please enter four different letters!!")
            continue

        l, r, u, d = received_letters
        return l, r, u, d
        break


def relist(lis):
    l = int(len(lis) ** (1 / 2))  # l = 3 or 4
    out = []
    row = 0
    while row <= l - 1:
        out.append([])
        col = 0
        while col <= l - 1:
            out[row].append(lis[row * l + col])
            col += 1
        row += 1
    return out


def move(out, pos_0_row, pos_0_col):
    choice = getValidChoice(out, pos_0_row, pos_0_col)
    while True:
        try:
            result = input("Enter your move {} > ".format(choice))
            if result == u:
                out[pos_0_row + 1][pos_0_col], out[pos_0_row][pos_0_col] \
                    = out[pos_0_row][pos_0_col], out[pos_0_row + 1][pos_0_col]
                break
            elif (result == d) and (pos_0_row - 1 >= 0):
                out[pos_0_row - 1][pos_0_col], out[pos_0_row][pos_0_col] \
                    = out[pos_0_row][pos_0_col], out[pos_0_row - 1][pos_0_col]
                break
            elif (result == r) and (pos_0_col - 1 >= 0):
                out[pos_0_row][pos_0_col - 1], out[pos_0_row][pos_0_col] \
                    = out[pos_0_row][pos_0_col], out[pos_0_row][pos_0_col - 1]
                break
            elif result == l:
                out[pos_0_row][pos_0_col + 1], out[pos_0_row][pos_0_col] \
                    = out[pos_0_row][pos_0_col], out[pos_0_row][pos_0_col + 1]
                break
            else:
                print(
                    "Please follow the instruction to enter!! Please enter a letter again!")
        except:
            print("Please follow the instruction to enter!!")


def isSolvable_8(lis):
    sum_inversions = 0  # The number of inversions
    for i in range(len(lis)):
        if lis[i] == 0:
            pass
        else:
            for j in range(0, i):
                if lis[j] > lis[i]:
                    sum_inversions += 1
    if sum_inversions % 2 == 0:
        return True
    else:
        return False


def isSolvable_15(lis):
    sum_inversions = 0  # The number of inversions
    for i in range(len(lis)):
        if lis[i] == 0:
            indx_0 = i
        else:
            for j in range(0, i):
                if lis[j] > lis[i]:
                    sum_inversions += 1

    row_0 = indx_0 // 4  # Get which row the blank is set
    if (sum_inversions % 2 == 0) and ((3 - row_0) % 2 == 0):
        return True
    elif (sum_inversions % 2 != 0) and ((3 - row_0) % 2 != 0):
        return True
    return False


def print_puzzle(out):
    l = len(out)  # l = 3 or 4
    row = 0
    while row <= l - 1:

        col = 0
        while col <= l - 1:
            num = out[row][col]
            print("%-3s" % num, end="")
            # Get the position of " "
            if out[row][col] == " ":
                pos_0_row = row
                pos_0_col = col
            col += 1

        print()
        row += 1
    return pos_0_col, pos_0_row


def getValidChoice(out, pos_0_row, pos_0_col):
    k = len(out) - 1  # k = 2 or 3
    choice = []
    if pos_0_row < k:  # Exist a adjacent tile below " "
        choice.append("up-%s" % u)
    if pos_0_row > 0:  # Exist a adjacent tile above " "
        choice.append("down-%s" % d)
    if pos_0_col < k:  # Exist a adjacent tile right " "
        choice.append("left-%s" % l)
    if pos_0_col > 0:  # Exist a adjacent tile left " "
        choice.append("right-%s" % r)
    return choice


def isSuccess(out, count):
    l = len(out)
    match = 0
    for row in range(l):
        for col in range(l):
            if (out[row][col] != row * l + (col + 1)) and (out[l - 1][l - 1] != " "):
                return
            elif out[row][col] == row * l + (col + 1):
                match += 1
    if out[l - 1][l - 1] == " ":
        match += 1
    if match == l ** 2:
        print("Congratulations! You solved the puzzle in %d moves!" % count)
        return True


def puzzle_8():
    print("*" * 80)
    print("Welcome to 8-puzzle game...")
    print("-" * 80)
    # Create a list include 0~8
    lis = [x for x in range(9)]
    while True:

        shuffle(lis)  # Shuffle positions randomly
        # If the shuffled list solvable, generating process will break
        if isSolvable_8(lis):
            break

    lis[lis.index(0)] = " "  # Replace the 0 with " "

    out = relist(lis)  # 3 x 3 [[],[],[]]

    pos_0_col, pos_0_row = print_puzzle(out)

    count = 0
    while True:

        move(out, pos_0_row, pos_0_col)
        # Show the result after move
        pos_0_col, pos_0_row = print_puzzle(out)
        count += 1  # Caculate the steps

        if isSuccess(out, count):
            break


def puzzle_15():
    print("*" * 80)
    print("Welcome to 15-puzzle game...")
    print("-" * 80)

    # Create a list include 0~15
    lis = [x for x in range(16)]
    while True:
        shuffle(lis)  # Shuffle positions randomly
        # If the shuffled lis is solvable, generating process will break
        if isSolvable_15(lis):
            break

    lis[lis.index(0)] = " "  # Replace the 0 with " "

    out = relist(lis)  # 4 x 4 [[],[],[],[]]

    pos_0_col, pos_0_row = print_puzzle(out)

    count = 0
    while True:
        move(out, pos_0_row, pos_0_col)
        pos_0_col, pos_0_row = print_puzzle(out)  # Show the result after move
        count += 1  # Caculate the steps

        if isSuccess(out, count):
            break


# At the start of the game, display a brief introduction about the game.
print("<<< Introduction >>>")
print("-" * 80)
print("Sliding Puzzle Game for both 8 and 15 numbers.\n \
For an 8-number puzzle, it has a square-framed board consisting of 8 square tiles, numbered 1 to 8, initially placed in random order, \n \
While a 15-number puzzle there are 15 numbered square tiles, from 1 to 15.\n \
The board has an empty space where an adjacent tile can be slid to. \n \
The objective of the game is to re-arrange the tiles into a sequential order by their numbers (left to right, top to bottom) by repeatedly making sliding moves (left, right, up or down).")
print("-" * 80)
# Promote the user to enter four letters
l, r, u, d = direction_letters()
# Choose 8 or 15 puzzles or quit
while True:
    choice = input(
        "Enter “1” for 8-puzzle, “2” for 15-puzzle or “q” to end the game > ")
    if choice == "1":
        puzzle_8()
    elif choice == "2":
        puzzle_15()
    elif choice == "q":
        print("Bye!")
        break
    else:
        print("Enter again!")
