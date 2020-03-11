from math import *

name = input("What's your name?")
print()
print("Welcome to interactive python, {} !".format(name))
print()
while True:
    
    scirpt = input(">>>")
    

    if scirpt == "quit":
        break
    
    try:
        print(eval(scirpt))

    except:
        try:
            exec(scirpt)
        except Exception as e:
            print(e)

print()
print("Bye, {}".format(name))
