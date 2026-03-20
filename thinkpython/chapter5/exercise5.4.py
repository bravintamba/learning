import turtle


def make_turtle(delay=0, height=200):
    width = height * 4
    turtle.setup(width=width, height=height)
    turtle.speed(0)
    turtle.hideturtle()
    if delay == 0:
        turtle.tracer(0, 0)
    else:
        turtle.tracer(1, delay)
    turtle.penup()
    turtle.goto(-width / 2 + 20, -height / 3)
    turtle.pendown()


def forward(distance):
    turtle.forward(distance)


def left(angle):
    turtle.left(angle)


def draw_sierpinski(length, depth):
    if depth == 0:
        for _ in range(3):
            forward(length)
            left(120)
    else:
        draw_sierpinski(length / 2, depth - 1)
        forward(length / 2)
        draw_sierpinski(length / 2, depth - 1)
        left(120)
        forward(length / 2)
        left(240)
        draw_sierpinski(length / 2, depth - 1)
        left(240)
        forward(length / 2)
        left(120)


if __name__ == '__main__':
    make_turtle(delay=0, height=200)
    draw_sierpinski(100, 3)
    turtle.update()
    turtle.done()