from PIL import Image

from__future__import print_function
print(im.format, im.size, im.mode)

im = Image.open("kitten.jpg")
source = im.split()

R, G, B = 0, 1, 2

mask = source[R].point(lambda i: i < 100 and 255)

out = source[G].point(lambda i: i * 0.7)

source[G].paste(out, None, mask)

im = Image.merge(im.mode, source)

