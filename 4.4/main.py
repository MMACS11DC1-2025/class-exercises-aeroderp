#Tutorial used: https://www.youtube.com/watch?v=iaWQoHIsQoc , https://www.askpython.com/python/examples/generate-random-colors , https://stackoverflow.com/questions/73663/how-do-i-terminate-a-script
import turtle
import math
import random

# Setup Screen
screen = turtle.Screen()
screen.bgcolor("#5C5C5C")

# Creating the turtle to draw a recursive flower with colours provided by the user
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

# grab user input for colour choices
answer = input("do you want random or own colours (random/own) ")
if answer == "own":
    colour_choices = {
        "red": {"color": "red"},
        "yellow": {"color": "yellow"},
        "orange": {"color": "darkorange"},
        "green": {"color": "green"},
        "blue": {"color": "blue"},
        "purple": {"color": "purple"}
    }

    choice = input("Choose a colour from the rainbow: ").lower()
    valid_input = False
    # if they wanted their own colour, had to make sure it was in the dictionary
    while not valid_input: # repeated until a valid colour was said
      if (choice == "red" or choice == "yellow" or choice == "orange"
      or choice == "green" or choice == "blue" or choice == "purple"):
        valid_input = True
      else:
        #if the colour was not in the dictionary, kept repeating the question
        print("Invalid color. Please choose from: red, yellow, orange, green, blue, purple")
        choice = input("Choose a colour from the rainbow: ").lower()
    # saved the colour data
    chosen_color = colour_choices[choice]

# if answer were not random or own, made them quit the program with a message
if answer != "random" and answer != "own":
  print("print random or own next time you run this program")
  quit()

# petals
def petal(radius, angle, color):
  t.fillcolor(color)
  t.begin_fill()
  for i in range(2):
    t.circle(radius, angle)
    t.left(180 - angle)
  t.end_fill()

# flower part of program, would go to the centre and redraw the new amounts of petals
# after every recursion, the screen would clear
def flower(angle):
  t.penup()
  t.goto(0, 0)
  t.pendown()
  t.setheading(angle) # rotates the image slightly after each recursion
  t.clear()

# petal total was subtracted once until reached base case
def recursive(petal_amount, petal_total, radius, count=0): 
    
    count += 1  # count amount of recursion
    # after reaching base case, amount of recursions would be told
    if petal_amount == 0: # base case
        return count 
    if answer == "own": # used the colour the user requested
          color = chosen_color["color"]
    else: # used a random colour
          color = random_color()
    petal(radius, 60, color)
    t.left(360 / petal_total)
    
    return recursive(petal_amount - 1, petal_total, radius, count)

screen.tracer(0) # used for smooth animation
angle = 0
petal_count = int(input("How many petals do you want"))
# setting a maximum petal amount for recursion
if petal_count > 45:
  petal_count = 45
  print("petal count is too high, going back to the maximum petal amount")
# setting a minimum petal amount for recursion
elif petal_count < 2:
  petal_count = 10
  print("petal count is too low, going back to the minimum petal amount")
  
# counter to keep record of amount of recursion done
total_recursion = 0

try:
  # loops as long as there are 1 or more petals
  while petal_count > 0:
    flower(angle)
    recursion_amount = recursive(petal_count-1, petal_count, 200)
    # adds number to counter
    total_recursion += recursion_amount 
    angle += 1 # rotates the flower
    petal_count -= 1 # reduces petal count
    screen.update() # shows new drawing for new recursion
    turtle.delay(100) # slows down animation so you can see the recursion
except turtle.Terminator:
  print("Closed")

# points out the amount of recursions made
print(str(total_recursion) + " recursions were made")
