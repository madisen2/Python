import numpy as np
import Image

img = Image.open('chris.png').convert('RGBA')
arr = np.array(img)

flat_arr = arr.ravel()
