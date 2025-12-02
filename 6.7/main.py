from PIL import Image
import time
t0 = time.time()
def colour(r, g, b):
    if r <= 100 and g <= 200 and b <= 250:
        return "blue"
    else:
        return "other"


blue_pixels = []

image_list = ["ocean1.png", "ocean2.jpg", "ocean3.jpg" "ocean4.jpg" "ocean5.webp" "ocean6.png" "ocean7.png" "ocean8.png" "ocean9.png" "ocean10.png"]

for image in image_list:
    file = Image.open("6.7/" + image)
    width = file.width
    height = file.height
    jb_image = file.load()


    for x in range(width):
        for y in range(height):
            r = jb_image[x, y][0]
            g = jb_image[x, y][1]
            b = jb_image[x, y][2]
            
            if colour(r,g,b) == "blue":
                blue_pixels.append(jb_image[x,y])
    t1 = time.time()
    time_taken = t1 - t0
    percent_blue = (len(blue_pixels)/(width*height))*100
    timing = "This program took {:.2f} seconds to run.".format(time_taken)
    print(timing)
    print("there are " + str(len(blue_pixels)) + " blue pixels in the image")
    print("there are " + str(width*height) + " total pixels in the image")
    percentage = "the percentage of blue pixels is {:.2f}%".format(percent_blue)
    print(percentage)
    image_output.save("ocean_output.png", "png")