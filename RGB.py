from PIL import Image, ImageFilter

im=Image.open('chris.png')

im.show()

im_sharp=im.filter(ImageFilter.SHARPEN)

im_sharp.save('chris.png','JPEG')

r,g,b=im_sharp.split()

