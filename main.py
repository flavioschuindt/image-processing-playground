import sys
from math import sqrt, pow
from PIL import Image


def complement(pixels, size):

    width, height = size
    my_pixels = []

    for j in range(height):
        for i in range(width):
            current_pixel = 255 - pixels[i, j]
            my_pixels.append(current_pixel)

    return my_pixels

def black_white(pixels, size):

    width, height = size
    my_pixels = []

    for j in range(height):
        for i in range(width):
            current_pixel = 0 if pixels[i, j] < 128 else 255
            my_pixels.append(current_pixel)

    return my_pixels

def mean_filter(pixels, size):

    # Apply a mean filter with a 2x2 kernel

    width, height = size
    my_pixels = []

    for j in range(height):
        for i in range(width):
            neighboors = []

            # right neighboor
            try:
                neighboors.append(pixels[i, j+1])
            except:
                pass

            # left neighboor
            try:
                neighboors.append(pixels[i, j-1])
            except:
                pass

            # up neighboor
            try:
                neighboors.append(pixels[i-1, j])
            except:
                pass

            # bottom neighboor
            try:
                neighboors.append(pixels[i+1, j])
            except:
                pass

            # upper-left neighboor
            try:
                neighboors.append(pixels[i-1, j-1])
            except:
                pass

            # upper-right neighboor
            try:
                neighboors.append(pixels[i-1, j+1])
            except:
                pass

            # bottom-left neighboor
            try:
                neighboors.append(pixels[i+1, j-1])
            except:
                pass

            # bottom-right neighboor
            try:
                neighboors.append(pixels[i+1, j+1])
            except:
                pass

            current_pixel = sum(neighboors) / len(neighboors)
            my_pixels.append(current_pixel)

    return my_pixels

def sharpening(pixels, size):

    width, height = size
    my_pixels = []

    for j in range(height):
        for i in range(width):

            try:
                dx = pixels[i+1, j] - pixels[i, j]
                dy = pixels[i, j+1] - pixels[i, j]

                mag = sqrt(pow(dx, 2) + pow(dy, 2))

                my_pixels.append(mag)
            except:
                my_pixels.append(pixels[i, j])

    return my_pixels

def create_image_from_pixels(pixels, mode, size):

    im = Image.new(mode, size)
    im.putdata(pixels)
    return im

if __name__ == "__main__":

    im = Image.open(sys.argv[1])
    im.show()

    gray = im.convert('L')
    gray_size = gray.size
    pixels = gray.load() # It's faster than use getpixel and putpixel
    gray.show()


    for operation in sys.argv[2:]:

        module = sys.modules[__name__]
        op = getattr(module, operation)

        new_pixels = op(pixels, gray_size)
        result = create_image_from_pixels(new_pixels, 'L', gray_size)
        result.save(operation+".png", "png")
        result.show()



