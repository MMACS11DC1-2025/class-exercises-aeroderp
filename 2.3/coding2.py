"""
Write an Olympic Judging program that outputs the average scores from 5 different judges. 

Each score is out of 10 points maximum. Half points are allowed (e.g. 7.5)

The program should take 5 inputs and output the final average score.

Example:

Judge 1: 5.5
Judge 2: 10
Judge 3: 7
Judge 4: 8.5
Judge 5: 9
Your Olympic score is 8.0
"""
score = 0
print("What is his/her score?")
one = float(input(" first score "))
two = float(input(" second score "))
three = float(input(" third score "))
four = float(input(" fourth score "))
five = float(input(" fifth score "))
score = (one + two + three + four + five) / 5
print("Your final score is " + str(score))