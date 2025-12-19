from PIL import Image
import time
# detects a  blueish-green pixel colour
# needed to adjust these values to withstand bright and dark light to get the best results
def is_target_colour(r, g, b):
    if b > r + 15 and b > g - 5: 
        return "blue"
    return "not blue"


# the ten images needing to be analyzed
image_list = ["ocean1.jpg", "ocean2.jpg", "ocean3.jpg", "ocean4.jpg", "ocean5.webp", "ocean6.webp", "ocean7.jpg", "ocean8.webp", "ocean9.jpg", "ocean10.jpg"]

# master list to store each image and the amount of blue pixels in each image
results = []

for i in range(len(image_list)):
    t0 = time.time() # starting the timer to to measure the time taken to analyze each image
    image = image_list[i]
    file = Image.open("6.7/" + image) # opening the images
    blue_pixels = 0 # counter for the number of blue pixels in each image
    width = file.width  
    height = file.height
    jb_image = file.load() # loading the images

    
    for x in range(width):  
        for y in range(height): 
            r = jb_image[x, y][0]
            g = jb_image[x, y][1]
            b = jb_image[x, y][2]
            
            # the formula needed to weigh bluer pixels more heavily than lighter blue pixels or darker blue pixels
            
            if is_target_colour(r,g,b) == "blue":
                blue_pixels += ((b - ((r + g) / 2)) / 255) ** 0.5
    t1 = time.time() # ending the timer to measure the time taken to analyze each image
    
    time_taken = t1 - t0   # calculating the amount of time taken in each image
    percent_blue = (blue_pixels/(width*height))*100 # calculating the percentage of blue pixels in each image

    timing = "ocean" + str(i+1) +  " took {:.3f} seconds to scan every pixel in the image.".format(time_taken)
    print(timing)
    print("there are " + str(blue_pixels) + " blue pixels in the image")
    print("there are " + str(width*height) + " total pixels in the image")
    print("the percentage of blue pixels is {:.2f}%\n".format(percent_blue))
    results.append((image, percent_blue))   # appending the image and the percentage of blue pixels in each image to the master list

# ranking the results
for i in range (len(results)): # sorting the master list from highest to lowest percentage of blue pixels
    biggest_index = i

    for j in range (i+1, len(results)): # finding the index of the image with the highest percentage of blue pixels
        if results[j][1] > results[biggest_index][1]:
            biggest_index = j
    results[i], results[biggest_index] = results[biggest_index], results[i] # swapping the current image with the image with the highest percentage of blue pixels

# binary search for image closest to minimum percentage but not below the minimum percentage
def search_min_results(results, min_percent):
    minimum = 0
    maximum = len(results)-1

    while minimum <= maximum: # binary search algorithm
        mid = (minimum + maximum) // 2

        if results[mid][1] >= min_percent: # if the percentage of blue pixels is greater than or equal to the minimum percentage, then the minimum index is updated to mid + 1
            minimum = mid + 1
        else:
            maximum = mid - 1 # if the percentage of blue pixels is less than the minimum percentage, then the maximum index is updated to mid - 1

    return minimum - 1
print("the image with the closest minimum is image " + str(search_min_results(results, 40)))

top5 = results[:5]  # top 5 images with the highest percentage of blue pixels
print("The top 5 images with the highest percentage of blue pixels are:")
for i in range(len(top5)):  # printing the top 5 images with the highest percentage of blue pixels
    print(i+1, top5[i][0], "{:.2f}%".format(top5[i][1]))

