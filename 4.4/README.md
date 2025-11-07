Fractal Art Generator:
Overview of the Project
This program is able to create beautiful fractal patterns using recursive algorithms and turtle graphics. Moreover, it enables users to create three types of visual arts: colorful spirals, floral patterns, and recursive fractal trees. The project also employs some core computer science concepts such as recursion, data structures, and user interaction.

Features:

Recursive Tree: Fractal tree that branches recursively with call counting

Spiral Patterns: Colorful concentric spirals with random color selection

Flower Designs: Preset flower designs based on dictionary settings

User Interaction: Dynamic input to customize all visual outputs

Call Counting: Keeps track and displays the total recursive function calls.
How to Run the Program

Prerequisites

Python 3.x installed
Turtle module (comes with standard Python installation)
Execution

python fractal_art.py

Usage:

Run the program

Choose between the following: spirals, flower, tree

Follow prompts to customize your selection:

Spirals: Select number of spirals (100-500)
Flower: Fill in flower type: rose, sunflower, marigold, daisy

Tree: Set recursion depth (2-8 levels)

Recursive Approach Explanation

Tree Function Recursion

The tree() function uses a classic binary recursion pattern:

Base case: if level==0 then the recursion stops and returns 1 (counting the call)

Recursive Case: For each branch, the function:

Draws the current branch segment

Makes two recursive calls for left and right subtrees

Reduces the problem size, decreasing level and branch length

Returns to original position for proper branching

Mathematical Foundation: Number of recursive calls is given by the formula 2^(depth+1) - 1, which shows exponential growth due to binary recursion.
Why Recursion Works
Self-similarity: Fractal trees repeat their branching pattern at every scale.

Problem Reduction: Each recursive call deals with a smaller subproblem - shorter branches, lower depth


Visual Outputs:

Test Case 1: Recursive Tree (Depth 4)

Input: tree with depth 4

Expected Output:

Brown fractal tree with clear branching structure

About 15 recursive calls
Symmetrical branching pattern

Actual Results:

tree_depth4.png

Recursive Calls: 15

Visual Quality: Fractal branching is clear, with good symmetry.

Performance: Fast rendering, immediate display

Test Case 2: Colorful Spirals

Input: spirals with 200 spirals

Expected Output:
Multi-colored spiral pattern growing outward

Smooth color transitions

Concentric circle pattern

Actual Results:

spirals_200.png

Visual Quality: Brightly colored, with smooth spiral growth

Performance: The rendering is slightly delayed because of 200 iterations.

Color Distribution: Random, but balanced color selection

Test Case 3: Sunflower Pattern
Input: flower with sunflower selection

Expected Output:

White floral pattern with petal-like structure

Decreasing circle sizes creating flower effect

Smooth rotational pattern

Actual Results:

daisy_pattern.png

Color Accuracy: Correct white coloration

Pattern Quality: Distinct floral pattern with arrangement of petals

Rendering: Smooth animation during drawing

Recursion Depth Discussion

Reasonable Depth Range

For this implementation, the reasonable recursion depth range is 2 to 8:

Too Low (Depth < 2):

Depth 1: Single trunk with no branches-not a tree

Depth 2: Minimal branching, lacks fractal complexity

Why: Not enough levels to show recursive pattern

Too High (Depth > 8):

Depth 9+: 511+ recursive calls, very dense rendering
Depth 12+: 4095+ calls, potential performance issues

Why: Exponential growth results in too many function calls and visual clutter

Optimal Range (3-6):

Clear fractal structure without overcrowding

Manageable recursion call counts (7-63 calls)
Good visualization of recursion concept
Performance Implications
Depth 4: 15 calls - Instant rendering
Depth 6: 63 calls - Fast rendering
Depth 8: 255 calls - Noticeable delay
Depth 10: 1023 calls - Very large delay


Testing and Debugging Process

Test Strategy

Unit Testing: Test each pattern type separately

Boundary Value Testing: Test the minimum and maximum values for inputs

Error Handling: Test invalid inputs weird cases

Visual Validation: Check the output matches expected patterns

Test Cases Executed

Test Case\tInput\tExpected\tActual\tStatus
TC1	tree, depth = 2,	7 calls, baisc tree, good tree	

TC2	trees, depth = 8,	511 calls, complex tree, detailed tree	

TC3 Spirals, 150 Colorful spiral pattern, Correct pattern

TC4	flower, rose	Red flower	Red floral pattern 

TC5	invalid input	Error message	""Please type." message"	

Debugging Issues

Initial Tree Orientation: Fixed by adding t.left(90) to point upward

Color Selection: added dictionary look-up for consistent colors

Recursive Call Counting: Added return value accumulation to track calls

Input Validation: Added validation for numeric inputs Validation Approaches Manual Inspection: Visual verification of all the patterns Call Count Verification: Mathematical validation of recursive counts User Testing: Multiple test runs, each with different parameters Boundary Value Testing: Minimum/maximum value checking Technical Implementation Data Structures Dictionary: flower_settings holds color and size settings Lists: Color palettes for spiral patterns Recursive Stack: Implicit stack management for tree recursion Algorithms Binary Recursion: Tree function with two recursive calls per invocation Iterative drawing - spiral and flower patterns with loops Input Validation: Boundary checking and error handling Key Functions tree(branch_length,level): Recursively draws a fractal tree, counting calls User Input Handling With Validation Pattern-specific drawing routines Conclusion This project effectively employs recursive algorithms in visual Turtle graphics. The implementation was very clear on recursion, proper handling of the base case, problem size reduction, and meaningful return values. This program is interactive for the user and educational regarding concepts in computer science.

