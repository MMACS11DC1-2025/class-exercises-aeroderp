from PIL import Image
import time
def colour(r, g, b):
    if r <= 100 and g <= 200 and b <= 250:
        return "blue"
    else:
        return "other"



image_list = ["ocean1.jpg", "ocean2.jpg", "ocean3.jpg", "ocean4.jpg", "ocean5.webp", "ocean6.webp", "ocean7.jpg", "ocean8.webp", "ocean9.jpg", "ocean10.jpg"]

results = []

for i in range(len(image_list)):
    t0 = time.time()
    image = image_list[i]
    file = Image.open("6.7/" + image)
    blue_pixels = 0
    width = file.width
    height = file.height
    jb_image = file.load()

    
    for x in range(width):
        for y in range(height):
            r = jb_image[x, y][0]
            g = jb_image[x, y][1]
            b = jb_image[x, y][2]
            
            if colour(r,g,b) == "blue":
                blue_pixels += 1
    t1 = time.time()
    
    time_taken = t1 - t0
    percent_blue = (blue_pixels/(width*height))*100

    timing = "ocean" + str(i+1) +  " took {:.2f} seconds to run.".format(time_taken)
    print(timing)
    print("there are " + str(blue_pixels) + " blue pixels in the image")
    print("there are " + str(width*height) + " total pixels in the image")
    print("the percentage of blue pixels is {:.2f}%\n".format(percent_blue))
    results.append((image, percent_blue))

# ranking the results
for i in range (len(results)):
    biggest_index = i

    for j in range (i+1, len(results)):
        if results[j][1] > results[biggest_index][1]:
            biggest_index = j
    results[i], results[biggest_index] = results[biggest_index], results[i]

# binary search for minimum percentage wanted
def search_min_results(results, min_percent):
    minimum = 0
    maximum = len(results)-1

    while minimum <= maximum:
        mid = (minimum + maximum) // 2

        if results[mid][1] = min_percent:
            return mid
        elif results[mid][1] < min_percent:
            maximum = mid - 1
        else:
            minimum = mid + 1

    
    return -1
print(search_min_results(results, 30))

    