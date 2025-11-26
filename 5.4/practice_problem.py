from PIL import Image
   
file = Image.open("5.4/jelly_beans.jpg")
jb_image = file.load()


image_output = Image.open("5.4/jelly_beans.jpg")

width = file.width
height = file.height

for x in range(width):
    for y in range(height):
        r = jb_image[x, y][0]
        g = jb_image[x, y][1]
        b = jb_image[x, y][2]
        
        if 150 < r < 256 and 150 < g < 256 and 0 <= b < 150:
            image_output.putpixel ((x, y), (255, 255, 255))

image_output.save("jelly_beans_yellow_removed.png", "png")