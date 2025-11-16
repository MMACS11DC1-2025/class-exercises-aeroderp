from PIL import Image
image_clock = Image.open("clock.jpg").load()
image_output = Image.open("kid-green.jpg")
width = image_output.width
height = image_output.height
for i in range(width):
    for j in range(height):
        im_r = image_green[i, j][0]
        im_g = image_green[i, j][1]
        im_b = image_green[i, j][2]
