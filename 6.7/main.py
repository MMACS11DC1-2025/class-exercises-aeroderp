from PIL import Image
import time
t0 = time.time()
def colour(r, g, b):
    if 40 < r < 80 and 80 < g < 140 and b <= 150:
        return "blue"
    else:
        return "other"


file = Image.open("6.7/ocean.png")
jb_image = file.load()


image_output = Image.open("6.7/ocean.png")

blue_pixels = []

width = file.width
height = file.height

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