import time

t0 = time.time()

from PIL import Image
t1 = time.time()
   
file = Image.open("5.4/jelly_beans.jpg")
jb_image = file.load()


image_output = Image.open("5.4/jelly_beans.jpg")

width = file.width
height = file.height

yellow_pixels = 0

t2 = time.time()
for x in range(width):
    for y in range(height):

        r = jb_image[x, y][0]
        g = jb_image[x, y][1]
        b = jb_image[x, y][2]

        if r > 150 and g > 150 and b < 100:
            yellow_pixels += 1
t3 = time.time()

print(yellow_pixels)
print(width*height)

percent_yellow = 100*yellow_pixels/(width*height)
report = "There are {:0.3f} percent yellow jellybeans.".format(percent_yellow)
print(report)

module_load = t1-t0
image_open_load = t2-t1
loop = t3-t2
entire = t3-t0

timings = "It took {:.2f}s to import PIL, {:.2f}s to load the image, and {:.2f}s to do the loop. All in all it took {:.2f}s" \
".".format(module_load, image_open_load, loop, entire)
print(timings)