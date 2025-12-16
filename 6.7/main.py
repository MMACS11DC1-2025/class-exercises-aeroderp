from PIL import Image
import time
def is_target_colour(r, g, b):
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
            
            if is_target_colour(r,g,b) == "blue":
                blue_pixels += 1
    t1 = time.time()
    
    time_taken = t1 - t0
    percent_blue = (blue_pixels/(width*height))*100

    timing = "ocean" + str(i+1) +  " took {:.3f} seconds to run.".format(time_taken)
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

# binary search for image closest to minimum percentage but not below the minimum percentage
def search_min_results(results, min_percent):
    minimum = 0
    maximum = len(results)-1

    while minimum <= maximum:
        mid = (minimum + maximum) // 2

        if results[mid][1] >= min_percent:
            minimum = mid + 1
        else:
            maximum = mid - 1

    return minimum - 1
print("the image with the closest minimum is image " + str(search_min_results(results, 67)))

top5 = results[:5]
print("The top 5 images with the highest percentage of blue pixels are:")
for i in range(len(top5)):
    print(i+1, top5[i][0], "{:.2f}%".format(top5[i][1]))

