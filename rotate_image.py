from PIL import Image

im = Image.open("chris.jpg")
im.rotate(45).show()

