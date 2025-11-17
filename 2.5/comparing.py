#author - Greysen
#date = sept 29
#comparing our favourites

#open file
file = open("2.4/responses.csv")
file.readline()

#grab my info in the file opened
for i in range(20):
    file.readline()

#makes all of the info into a list
me = file.readline().strip().split(",")


for i in range(len(me)):
    me[i] = me[i].lower()

#initializing the variable
#ammount common is used to see how many favourites we have in common
ammtcommon = 0
#ammount not common is used to check what favourites we do not have in common
notcommon = []

#grabbing the inputs from the user with different questions
fvsubject = input("What is your favourite subject? ").lower().strip()
fvpet = input("What is your favourite pet? ").lower().strip()
fvmovie = input("What is your favourite genre of movies? ").lower().strip()
fvplace = input("What is your favourite place to eat nearby Killarney? ").lower().strip()
fvsport = input("What is your favourite sport to do? ").lower().strip()
#adding a counter to my counter variable for every response that relates to my response to the question
#append is used to keep check for every response that does not relate to my response to the question
if fvsubject in me:
    ammtcommon += 1
else:
    notcommon.append(me[4])
if fvpet in me:
    ammtcommon += 1
else:
    notcommon.append(me[3])
if fvmovie in me:
    ammtcommon += 1
else:
    notcommon.append(me[8])
if fvplace in me:
    ammtcommon += 1
else:
    notcommon.append(me[9])
if fvsport in me:
    ammtcommon += 1
else:
    notcommon.append(me[5])

#prints out a response depending on how many responses from the user relates to mine
if ammtcommon <= 1:
    print("We are nothing alike")
elif ammtcommon <= 4:
    print("We are somewhat alike")
elif ammtcommon == 5:
    print("We are the exact same person!")

#this shows the ammount of responses we have in common together
print("You have " + str(ammtcommon) + " favourites in common with me.")

#takes the input that we did not have in common and tells the user I also like --response(not in common)-- (up to three responses)
if len(notcommon) > 0:
    if len(notcommon) == 1:
        print("Though, I also like " + notcommon[0])
    elif len(notcommon) == 2:
        print("Though, I also like " + notcommon[0] + ", and" +  notcommon[1])
    elif len(notcommon) >= 3:
        print("Though, I also like " + notcommon[0] + ", " +  notcommon[1] + ", and " +  notcommon[2])

#practice run, correct:
'''What is your favourite subject? Science
What is your favourite pet? rabbit
What is your favourite genre of movies? fantasy/sci-fi
What is your favourite place to eat nearby Killarney? Chipotle
What is your favourite sport to do? Badminton
We are the exact same person!
You have 5 favourites in common with me.'''

#practice run, error:
'''What is your favourite subject? Science
What is your favourite pet? rabbit
What is your favourite genre of movies? fantasy/sci-fi
What is your favourite place to eat nearby Killarney? Chipotle
What is your favourite sport to do? Badminton!
We are somewhat alike
You have 4 favourites in common with me.
Though, I also like badminton'''