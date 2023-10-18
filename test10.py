from turtle import *
speed(0)
hideturtle()

def line(sx,sy,dx,dy):
    up()
    goto(sx,sy)
    down()
    goto(dx,dy)

while dx <= 200:
    line(sx,sy,dx,dy)
    sy = sy - 10
    dx = dx + 10
done()

