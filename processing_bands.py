from __future__ import print_function

from PIL import Image
im = Image.open("chris.jpg")

source = im.split()

R, G, B = 0, 1, 2

mask = source[R].point(lambda i: i <100 and 255)

out = source[G].paste(out, None, mask)

im = Image.merge(im.mode, source)

im.show()
