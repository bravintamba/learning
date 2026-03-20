import turtle

def rectangle(width, height):
    for i in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)

rectangle(100, 50)
turtle.done()                   