from PIL import Image
im=Image.open("chris.jpg")

print(im.format,im.size,im.mode)

im.show()

import os, sys

for infile in sys.argv[1:]:
	f, e = os.path.splitext(infile)
	outfile = f + ".jpg"
	if infile != outfile:
		try:
			Image.open(infile).save(outfile)
		except IOError:
			print("cannot convert", infile)


for infile in sys.argv[1:]:
	try:
		with Image.open(infile) as im:
			print(infile, im.format, "%dx%d" % im.size, im.mode)

box = (100, 100, 400, 400)

region = im.crop(box)

	except IOError:
		pass
