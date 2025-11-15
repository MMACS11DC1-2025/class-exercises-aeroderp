#Tutorial used: https://www.youtube.com/watch?v=iaWQoHIsQoc was only used for the image of the flower, not recursion
import turtle
import math
import random

# Setup Screen
screen = turtle.Screen()
screen.bgcolor("#5C5C5C")


# Creating the turtle
t = turtle.Turtle()
t.speed(15)
t.hideturtle()
t.pensize(2)

# random color maker
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

# petals
def petal(radius, angle, color):
  t.fillcolor(color)
  t.begin_fill()
  for i in range(2):
    t.circle(radius, angle)
    t.left(180 - angle)
  t.end_fill()

# flower
def flower(angle):
  t.penup()
  t.goto(0, 0)
  t.pendown()
  t.setheading(angle)
  t.clear()
  
def recursive(petal_ammount, petal_total, radius):
  if petal_ammount == 0:
    return
  color = random_color()
  t.color(color)
  petal(radius, 60, color)
  t.left(360 / petal_total)
  recursive(petal_ammount-1, petal_total, radius)


screen.tracer(0)
angle = 0
petal_count = 16
try:
  while petal_count > 0:
    flower(angle)
    recursive(petal_count-1, petal_count, 200)
    angle += 1
    petal_count -= 1
    screen.update()
    turtle.delay(100)
except turtle.Terminator:
  print("Closed")
