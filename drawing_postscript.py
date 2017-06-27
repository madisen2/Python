from PIL import Image
from PIL import PSDraw

im = Image.open("chris (copy).jpg")
title = "chris"

box = (1*72, 2*72, 7*72, 10*72)

ps = PSDraw.PSDraw()
ps.begin_document(title)

ps.image(box, im, 75)
ps.rectangle(box)

ps.setfont("HelveticaNarrow-Bold",36)
ps.text((3*72, 4*72), title)

ps.end_document()
