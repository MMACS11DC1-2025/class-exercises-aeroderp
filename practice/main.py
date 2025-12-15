list = [4,2,6,7,1,5,2,3]
list2 = list[:]
highest = []
for i in range (int(list2)):
    if list[i] <= 0:
        ammount = list[i]
        highest += ammount
        