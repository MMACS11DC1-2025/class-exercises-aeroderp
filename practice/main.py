scores = [4,2,6,7,1,5,2,3]
for i in range (len(scores)):

    smallest_score = scores[i]
    smallest_index = i
    for j in range (i+1, len(scores)):
        if scores [j] < smallest_score:
            smallest_score = scores[j]
            smallest_index = j
    scores[i], scores[smallest_index] = scores[smallest_index], scores[i],
print(scores)

