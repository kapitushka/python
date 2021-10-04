from turtle import *
shape("turtle")

speed('fastest')
bgcolor("black")
right(-90)
angle = 60
def branch(size, level):
    if level > 0:
        colormode(255)
        pencolor(0, 255//level, 0)
        forward(size)
        right(angle )
        branch(0.8 * size, level-1)
        pencolor(0, 255//level, 0)
        left(2 * angle)
        branch(0.8 * size, level-1)
        pencolor(0, 255//level,0)
        right(angle)
        forward(-size)
width(4)
branch(70, 7)
done()
