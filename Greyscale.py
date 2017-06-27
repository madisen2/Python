from PIL import Image

def create_image(i,j):
    image=Image.new("RGB",(i,j),"white")
    return image

def convert_greyscale(image):

    width,height=image.size

    new=create_image(width,height)
    pixels=new.load()

    for i in range(width):
        for j in range(height):
            pixel=get_pixel(image,i,j)

            red=pixel[0]
            green=pixel[1]
            blue=pixel[2]

            gray=(red*0.229)+(green*0.587)+(blue*00.114)

            pixels[i,j]=(int(gray),int(gray),int(gray))

            return new