import sys
from PIL import Image

im=Image.open("chris.jpg")

for infile in sys.argv[1:]:
	try:
		with Image.open(infile) as im:
			print(infile, im.format, "%dx%d" % im.size, im.mode)
	except IOError:
		pass

