import turtle
import math

def rectangle(t, width, height):
    for i in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)

def triangle(t, r, angle):
    side_edge = 2 * r * math.sin(math.radians(angle / 2))
    base_angle = (180 - angle) / 2

    t.forward(r)
    t.left(180 - base_angle)
    t.forward(side_edge)
    t.left(180 - base_angle)
    t.forward(r)
    t.left(180)

def draw_pie(t, n, r):
    angle = 360 / n
    for _ in range(n):
        triangle(t, r, angle)
        t.left(angle)

bob = turtle.Turtle()
bob.speed(6)

rectangle(bob, 80, 40)

bob.penup()
bob.goto(150, 0) 
bob.pendown()

draw_pie(bob, 7, 60)

turtle.done()

