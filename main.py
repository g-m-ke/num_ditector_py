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

    blurred.save(imagename)


def GrayScale (imagename):
    try:
        tatras = Image.open(imagename)
        
    except IOError:
        print("Unable to load image")
        sys.exit(1)
        
    grayscale = tatras.convert('L')
    grayscale.save(imagename)


def Crop (imagename, inp1 , inp2, inp3, inp4):
    try:
        tatras = Image.open(imagename)

    except IOError:
        print("Unable to load image")
        sys.exit(1)
        
    cropped = tatras.crop((inp1, inp2, inp3, inp4))
    cropped.save(imagename)
    

def Rotate(imagename, dig):
    try:
        tatras = Image.open(imagename)

    except IOError:
        print("Unable to load image")
        sys.exit(1)
        
    rotated = tatras.rotate(dig)
    rotated.save(imagename)
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
     
    tatras.save(imagename)
def Help (command):
    pass
def image_Save (In,Rin):
    try:
        tatras = Image.open(In)
        
    except IOError:
        print("Unable to load image")
        sys.exit(1)
    tatras.save(Rin)
def Open (imagename):
    try:
        img = Image.open(imagename)
        
    except IOError:
        print("Unable to load image")    
        sys.exit(1)
    img.save("new"+imagename)
    return imagename
imagename = ""
realimagename = ""
CMD = input()
command = CMD.split("|")

while command[0] != "Exit_Save" and command[0] != "Exit_Don't_Save":
    ##########@@@@@@@@@##########
    
    if command[0] == "Blur"and len(command)==2 and imagename != "" and imagename != "Unable to load image":
        Blur(imagename)
        print("command Ended write Another:\n")
    elif command[0] == "GrayScale"and len(command)==2 and imagename != "" and imagename != "Unable to load image":
        GrayScale(imagename)
        print("command Ended write Another:\n")
        
    elif command[0] == "Open"and len(command)==2 :
        Open(command[1])
        imagename = "new"+Open(command[1])
        realimagename = Open(command[1])
        print("command Ended write Another:\n")
    elif command[0] == "Rotate"and len(command)==2 and imagename != "" and imagename != "Unable to load image":
        Rotate(imagename,-(int(command[1])))
        print("command Ended write Another:\n")
    elif command[0] == "Crop"and len(command)==5 and imagename != "" and imagename != "Unable to load image":
        Crop(imagename,int(command[1]),int(command[2]),int(command[3]),int(command[4]))
        print("command Ended write Another:\n")
        
    elif command[0] == "WaterMark"and len(command)==6 and imagename != "" and imagename != "Unable to load image":
        WaterMark(imagename,command[1],int(command[2]),command[3],int(command[4]),int(command[5]))
        print("command Ended write Another:\n")
        
    elif command[0] == "Help"and len(command)==2:
        if command[1] == " " or command[1] == '':
            print ("OK lets start this app built to help you with editing a photo \n\n to command you should write: \n Command|values \n\n Command: is name of the command that you want to do like Blur, Rotate,... \n | : you shoud put this between command and values \n value : is the inputs of the functions that you use \n\nto start editing write:\n Open|image_name\n\nTHANKS FOR USE ME")
        else:
            Help(command[1])
        print("command Ended write Another:\n")
    else:
        print("Wrong Command inputed!\n if you don't know how to use this app just write:\n Help| or Help|name_of_a_command")

    CMD = input()
    command = CMD.split("|")

if command[0] == "Exit_Save":
    #image_Save(imagename,realimagename)
    pass
else:
    #Del_Edits(imagename)
    pass









