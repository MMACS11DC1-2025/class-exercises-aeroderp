"""
Fractal Art Generator
A program that creates recursive fractal patterns using turtle graphics.
Includes spirals, flowers, and recursive trees with user customization.
"""

import turtle
import random

# Initialize turtle graphics environment
screen = turtle.Screen()
t = turtle.Turtle()
t.speed(0)  # Set to fastest drawing speed
screen.bgcolor("black")  # Set background to black
t.hideturtle()  # Hide turtle cursor for cleaner pictures

def tree(branch_length, level):
    """
    Recursively draws a fractal tree and returns multiple statistics.
    
    Arguements:
        branch_length (int): Length of the current branch segment
        level (int): Current recursion depth (decreases until base case)
    
    Returns:
        dict: Dictionary containing calls, levels, and branches statistics
    """
    # Base case: stop recursion when we reach depth 0 - no branches drawn
    if level == 0:
        return {"calls": 1, "levels": 1, "branches": 0}
    
    # Draw the main branch (this counts as 1 branch segment)
    t.forward(branch_length)
    current_branches = 1  # We just drew one branch segment
    
    # Draw right subtree
    t.right(20)
    right_stats = tree(branch_length * 0.7, level - 1)
    
    # Draw left subtree
    t.left(40)
    left_stats = tree(branch_length * 0.7, level - 1)
    
    # Return to original position
    t.right(20)
    t.backward(branch_length)
  
    # Only count the branches that were actually drawn in this call and its recursive calls
    total_branches = current_branches + right_stats["branches"] + left_stats["branches"]
    
    return {
        "calls": 1 + right_stats["calls"] + left_stats["calls"],
        "levels": max(right_stats["levels"], left_stats["levels"]) + 1,
        "branches": total_branches
    }

# grab user input for the design they want
answer = input("spirals, flower, or tree: ")

# spiral pattern, Creates colourful spirals
if answer == "spirals":
    # Colours for spiral pattern
    colors = ["red", "orange", "yellow", "green", "blue", "purple", 
              "pink", "cyan", "white", "lime", "magenta", "gold"]
    
    # Get user input for the anmount of spirals, boundaries apply
    spiral = int(input("How many spirals? (max is 500, min is 100) "))
    
    # Input validation to prevent spirals from taking more space than the screen provides
    if spiral > 500:
        print("Reducing to maximum 500 spirals")
        spiral = 500
    elif spiral < 100:
        print("Using minimum 100 spirals")
        spiral = 100
    
    # Draw spirals with increasing radius and random colors
    for i in range(spiral):
        t.color(random.choice(colors))  # Random color selection
        t.circle(i * 0.35)  # Increasing circle radius creating spirals
        t.left(5)  # Small rotation between circles

# FLOWER PATTERN: Draws flower patterns with different colours depending on user input
elif answer == "flower":
    # Dictionary storing flower configurations
    flower_settings = {
        "rose": {"color": "red", "size": 10},
        "sunflower": {"color": "yellow", "size": 12},
        "marigold": {"color": "darkorange", "size": 6},
        "daisy": {"color": "white", "size": 9}
    }

    # Get user flower choice
    choice = input("Choose a flower that has your favourite flower colour (rose, sunflower, marigold, daisy): ").lower()

    # Checking if valid input, if not, uses default colour
    if choice not in flower_settings:
        print("not available, using rose")
        choice = "rose"

    # Configure turtle with selected flower settings
    t.color(flower_settings[choice]["color"])  # Set color from dictionary
    t.speed(150)  # Fast drawing speed
    t.hideturtle()  # Hide cursor for cleaner display

    # Draw flower pattern using decreasing circle sizes
    for i in range(100):
        t.circle(flower_settings[choice]["size"] - i)  # Decreasing radius
        t.left(60)  # Rotation creates petal-like pattern

# TREE PATTERN: Draws recursive fractal tree with recursive counting
elif answer == "tree":
    # Configure tree drawing settings
    t.color("brown")  # Tree trunk color
    t.left(90)  # Point turtle upward for tree orientation
    t.penup()  # Lift pen to move without drawing
    t.backward(100)  # Move to starting position at bottom of screen
    t.pendown()  # Lower pen to start drawing
    
    # Get recursion depth from user with the suggested range
    level = int(input("How deep should the tree be? (2-8): "))
    
    # Input validation to prevent too many or too few branches
    if level > 8:
        print("Reducing to maximum branches: 8")
        level = 8
    elif level < 2:
        print("Increasing to minimum branches: 2")
        level = 2
    
    # Execute recursive tree function and get statistics
    stats = tree(80, level)  # 80 is initial branch length
    
    # Display multiple statistics
    print("Total recursive calls: {}".format(stats['calls']))
    print("Tree height (max depth): {}".format(stats['levels']))
    print("Total line segments drawn: {}".format(stats['branches']))

# used if user gives an invalid answer
else:
    print("Please type either 'spirals', 'flower', or 'tree'")
