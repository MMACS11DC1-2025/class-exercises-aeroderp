score = 0
print("Answer this. What is 9+1")
answer1 = input()
if answer1 == "10":
    print("correct")
    score += 1
else:
    print("wrong")
    
print("Answer this. What is 9-3")
answer2 = input()
if answer2 == "6":
    print("correct")
    score += 1
else:
    print("wrong)")
    
percent = score/2 * 100
print("your score is " + str(score) + "/2 or " + str(percent) + "%")
