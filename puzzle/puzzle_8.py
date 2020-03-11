from random import shuffle
from tools import *

print("*" * 80)
print("Welcome to 8-puzzle game...")
print("-" * 80)
# promote the user to enter four letters 
l,r,u,d = direction_letters()

# create a list include 0~8
lis = [x for x in range(9)]
while True:
    shuffle(lis)  # shuffle positions randomly
    if isSolvable_8(*lis):  # if the shuffled lis is not solvable, continue to shuffle the lis until it's solvable
        break
lis[lis.index(0)] = " "  # replace the 0 with " "

# 3 x 3 
i = 0
out = []
row = 0
while row <= 2:
    out.append([])
    col = 0
    while col <= 2:
        out[row].append(lis[i])           
        i += 1
        col += 1

    row += 1

def print_8_puzzle(out):  
    global pos_0_row
    global pos_0_col  
    row = 0
    while row <= 2:
        
        col = 0
        while col <= 2:
            num = out[row][col]
            print(num, end="")
            
            if out[row][col] == " ":
                pos_0_row = row
                pos_0_col = col
            
            col += 1
        print()
        row += 1

print_8_puzzle(out)

count = 0
while True:
    # get vaild choice to move
    choice = []   
    if pos_0_row < 2:
        choice.append("up-%s" % u)
    if pos_0_row > 0:
        choice.append("down-%s" % d)
    if pos_0_col < 2:
        choice.append("left-%s" % l)
    if pos_0_col > 0:
        choice.append("right-%s" % r)
    
    move(out,u,d,r,l,pos_0_row,pos_0_col,*choice)  
    # show the result after move
    print_8_puzzle(out)
    count += 1  # caculate the steps    
    
    if isSuccess_8(out,count):
        break



