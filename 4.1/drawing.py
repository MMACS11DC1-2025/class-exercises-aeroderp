import turtle
t = turtle.Turtle()

def draw_circle(x, y):
	t.penup()
	t.goto(x, y)
	t.pendown()
	t.circle(30)
	t.penup()
  
while True:
	command = input("What do you want me to do?")
	draw_circle(0, 0)
	if command == "stop":
		break 
	draw_circle(0, 0)
	draw_circle(100, 100)
	draw_circle(-70, 30)
   