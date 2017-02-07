from __future__ import print_function
from PIL import Image
im = Image.open("chris.jpg")

r, g, b = im.split()
im = Image.merge("RGB", (b, g ,r))
im.show()
