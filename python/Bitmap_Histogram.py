from PIL import Image


image = Image.open("lena.jpg")

width, height = image.size

amount = width * height


total = 0

bw_image = Image.new('L', (width, height), 0)

bm_image = Image.new('1', (width, height), 0)

for h in range(0, height):
    for w in range(0, width):
        r, g, b = image.getpixel((w, h))

        greyscale = int((r + g + b) / 3)
        total += greyscale

        bw_image.putpixel((w, h), gray_scale)


avg = total / amount

black = 0
white = 1

for h in range(0, height):
    for w in range(0, width):
        v = bw_image.getpixel((w, h))

        if v >= avg:
            bm_image.putpixel((w, h), white)
        else:
            bm_image.putpixel((w, h), black)

bw_image.show()
bm_image.show()
