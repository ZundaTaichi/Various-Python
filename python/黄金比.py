import turtle
from random import random

def draw_square(r) :
    t.fillcolor(random(),random(),random())
    t.begin_fill()
    for _ in range(4):
        t.fd(r)
        t.left(90)
        if _== 1:
            t.end_fill()
            t.fillcolor(random(),random(),random())
            t.begin_fill()
    t.circle(r,90)
    t.end_fill()
    return

if __name__ == '__main__':
    t = turtle.Turtle()
    t.hideturtle()
    t.up()
    t.goto(-130,50)
    t.down()
    t.pensize(3)
    scale = 0.618
    r = 50

    for _ in range(5):
        draw_square(r)
        r /= scale

    turtle.mainloop()