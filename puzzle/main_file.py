from tools import *
# At the start of the game, display a brief introduction about the game.
introduction()


# choose 8 or 15 puzzles
while True:
    result = input("Enter “1” for 8-puzzle, “2” for 15-puzzle or “q” to end the game >")
    if result == "1":
        exec(open("puzzle_8.py").read())
    elif result == "2":
        exec(open("puzzle_15.py").read())
    elif result == "q":
        break
    else:
        print("Enter again!")
        continue



