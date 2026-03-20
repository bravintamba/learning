import turtle
import math

def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = angle / n
    for i in range(n):
        t.forward(step_length)
        t.left(step_angle)

def petal(t, r, angle):
    for i in range(2):
        arc(t, r, angle)
        t.left(180 - angle)

def flower(t, n, r, angle):
    for i in range(n):
        petal(t, r, angle)
        t.left(360.0 / n)

def move(t, length):
    t.penup()
    t.forward(length)
    t.pendown()

bob = turtle.Turtle()
bob.speed(0)

move(bob, -150)
flower(bob, 7, 60.0, 60.0)

move(bob, 150)
flower(bob, 10, 40.0, 80.0)

move(bob, 150)
flower(bob, 20, 140.0, 20.0)

turtle.done()