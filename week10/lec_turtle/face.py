from basic_graph import *


def move(x, y, head=0):
    tt.up()
    tt.goto(x, y)
    tt.down()
    tt.setheading(head)


def eye(r=50):

    move(-100, 100-r)
    circle(r)
    move(-100, 100-r/2)
    circle(r/2)

    move(100, 100 - r)
    circle(r)
    move(100, 100 - r / 2)
    circle(r / 2)


def eyebrow(l=100):
    move(-100,170,30)
    tt.forward(l/2)
    move(-100,170,210)
    tt.forward(l/2)

    move(100, 170, 180-30)
    tt.forward(l / 2)
    move(100, 170, 360-30)
    tt.forward(l / 2)


def mouth(r=100):
    tt.forward(r)
    move(0,0,180)
    tt.forward(r)
    tt.left(90)
    arc(r, 180)
    tt.left(90)
    tt.forward(r)


def tongue():
    pass


eyebrow()
eye()
mouth()
tt.screen.mainloop()