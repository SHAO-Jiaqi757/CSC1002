from turtle import Turtle
import math

g_pen = None

def square(length):
    polygon(4, length)

def polygon(side, length, span=360):
    angle = span/side
    for i in range(side):
        g_pen.forward(length)
        g_pen.left(angle)

def circle(r):
    arc(r, 360)

def arc(r, span):
    cir = 2 * math.pi * r * span/360
    side = int(cir/3)
    length = cir/side
    polygon(side, length, span)

def move(x, y, head=0):
    g_pen.up()
    g_pen.goto(x,y)
    g_pen.down()
    g_pen.setheading(head)

def eye(x, y, sz):
    # outer circle
    move(x, y-sz)
    circle(sz)
    
    # inner circle
    move(x,y-sz/2)
    circle(sz/2)

if __name__ == "__main__":
    g_pen = Turtle()
    g_pen.speed(0)
    move(-50,0)
    square(100)
    move(-100,-100)
    polygon(6,200)
    move(0,0)
    circle(50)
    arc(50,180)
    eye(100, 100, 80)
    eye(-100, 100, 80)
    g_pen.screen.mainloop()
