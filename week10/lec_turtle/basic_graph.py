import turtle
import  math
tt = turtle.Turtle()
def polygon(side,  length, degree=360):
    angle = degree/side
    for i in range(side):
        tt.forward(length)
        tt.left(angle)


def circle(radius):
    arc(radius,360)

def arc(r, angle):
    c = 2*math.pi*r*angle/360
    side = int(c)
    length = c/side
    polygon(side, length, angle)


