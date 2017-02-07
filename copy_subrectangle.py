from __future__ import print_function


from PIL import Image
im = Image.open("chris.jpg")
print(im.format, im.size, im.mode)


box =(100, 100, 400, 400)
region = im.crop(box)
region = region.transpose(Image.ROTATE_180)
im.paste(region, box)

im.show()



