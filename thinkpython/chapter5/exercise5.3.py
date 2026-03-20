import turtle


def make_turtle(delay=0):
    turtle.setup(width=800, height=800)
    turtle.speed(0)
    turtle.hideturtle()
    if delay == 0:
        turtle.tracer(0, 0)
    else:
        turtle.tracer(1, delay)
    turtle.penup()
    turtle.goto(-200, 0)
    turtle.pendown()


def forward(distance):
    turtle.forward(distance)


def left(angle):
    turtle.left(angle)


def right(angle):
    turtle.right(angle)


def koch(x):
    if x < 5:
        forward(x)
    else:
        koch(x / 3)
        left(60)
        koch(x / 3)
        right(120)
        koch(x / 3)
        left(60)
        koch(x / 3)


if __name__ == '__main__':
    make_turtle(delay=0)
    koch(120)
    turtle.update()
    turtle.done()s