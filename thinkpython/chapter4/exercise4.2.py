import turtle

def rhombus(width, height):
    for i in range(2):
        turtle.forward(width)
        turtle.left(60)
        turtle.forward(height)
        turtle.left(120)

rhombus(100, 50)
turtle.done()