from random import shuffle
from tools import *
# create a list include 0~8
lis = [x for x in range(9)]
shuffle(lis)  # shuffle positions randomly

# 3 x 3 
i = 0
out = []
row = 1
while row <= 3:
    out.append([])
    col = 1
    while col <= 3:
        out[row-1].append(lis[i])
        
        if out[row-1][col-1] == 0:
            pos_0_row = row
            pos_0_col = col
            
        i += 1
        col += 1

    row += 1

print_8_puzzle(out)

#  Prompt user to enter the 4 letters used for the left, right, up and down moves.
l = input("enter a letter for the left moves:")
r = input("enter a letter for the right moves:")
u = input("enter a letter for the up moves:")
d = input("enter a letter for the down moves:")

if (pos_0_row == 2) and (pos_0_col==2):
    move_lrud(out,l,r,u,d)
    print_8_puzzle(out)

# if pos_0_row == 




# row = 1
# while row <= 3:
    
#     col = 1
#     while col <= 3:
#         print(lis[i], end="")
#         i += 1

#         col += 1

#     print()
#     row += 1

