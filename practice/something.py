# Binary Search
# Author: Angelica Lim
# Date: April 5, 2018

# Define a function that searches a list_of_lists for query
# Requires that the list_of_lists be sorted
def search(list_of_lists, query):

    # Define indices of search space
    search_start_index = 0
    search_end_index = len(list_of_lists)-1

    # As long as our search space exists
    while search_start_index <= search_end_index:

        # Calculate centre of search space
        midpoint = int((search_start_index+search_end_index)/2)

        # If the element in the centre is what we're looking for, return!
        if list_of_lists[midpoint][0] == query:
            return list_of_lists[midpoint][1]

        # If what we're looking for is greater than the centre value
        elif list_of_lists[midpoint][0] < query:

            # Cut out the entire left-hand side of our search space
            search_start_index = midpoint+1

        # If our query is less than our centre value
        else:
            # Cut out the entire right-hand side of our search space
            search_end_index = midpoint-1

    # If we still haven't found it, return -1
    return -1

ages = [[30,"Rihanna"],[31,"Drake"], [33, "Katy Perry"],[36,"Beyonce"]]

print(search(ages, 33))
print(search(ages, 25))