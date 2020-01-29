import PIL
from PIL import Image , ImageFilter, ImageDraw, ImageFont
import sys

def Blur (imagename):
    try:
        img = Image.open(imagename)
        
    except IOError:
        print("Unable to load image")    
        sys.exit(1)

    blurred = img.filter(ImageFilter.BLUR)

    blurred.save("blurred.png")


def GrayScale (imagename):
    try:
        tatras = Image.open(imagename)
        
    except IOError:
        print("Unable to load image")
        sys.exit(1)
        
    grayscale = tatras.convert('L')
    grayscale.save("grayscale.png")


def Crop (imagename, inp1 , inp2, inp3, inp4):
    try:
        tatras = Image.open(imagename)

    except IOError:
        print("Unable to load image")
        sys.exit(1)
        
    cropped = tatras.crop((inp1, inp2, inp3, inp4))
    cropped.save('tatras_cropped.jpg')
    

def Rotate(imagename, dig):
    try:
        tatras = Image.open(imagename)

    except IOError:
        print("Unable to load image")
        sys.exit(1)
        
    rotated = tatras.rotate(dig)
    rotated.save('rotated.jpg')
def WaterMark (imagename,fontName,fontSize,text,x,y):
    #sample font:"arial.ttf"
    try:
        tatras = Image.open(imagename)

    except:
        print("Unable to load image")
        sys.exit(1)
        
    idraw = ImageDraw.Draw(tatras)
    

    font = ImageFont.truetype(fontName, size=fontSize)

    idraw.text((x, y), text, font=font)
     
    tatras.save('watermarked.png')
def Help (command):
    pass


Blur("surf.jpg")
GrayScale("surf.jpg")
Crop("surf.jpg",200,200,500,500)
Rotate("surf.jpg",-35)
WaterMark("surf.jpg","arial.ttf",200,"hello",40,300)











