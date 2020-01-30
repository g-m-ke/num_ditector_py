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


def Crop (imagename, x1 , y1, x2, y2):
    try:
        tatras = Image.open(imagename)

    except IOError:
        print("Unable to load image")
        sys.exit(1)
        
    cropped = tatras.crop((x1, y1, x2, y2))
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
    if command == "Open":
        print("Open is an function to start editing a photo \n\n to use this command you should write :\n\n Open|image_name \n sample: Open|surf.jpg\n\n to start editing another photo middle of another editing write:\n\
Edit_Save| or Edit_Don't_Save|\n Open|image2_name")

    elif command == "Show":
        print("Show is function to see the result of edits to use you should write:\n Show|")

    elif command == "Blur":
        print("Blur is function to make the picture blur to use you should write:\n Blur|")

    elif command == "GrayScale":
        print("GrayScale is function to make the picture gray like old pictures to use you should write:\n GrayScale|")

    elif command == "Rotate":
        print("Rotate is function to rotate the picture in Clockwise to use you should write:\n Rotate|Degree")

    elif command == "WaterMark":
        print("WaterMark is function to write something on picture to use you should write:\n WaterMark|fontname,fontsize,text,x,y")

    elif command == "Crop":
        print("Crop is function to crop a part of picture to use you should write:\n Crop|x1,y1,x2,y2")

    elif command == "Exit_Save":
        print("Exit_Save is function to save edits and exit to use you should write:\n Exit_Save")

    elif command == "Exit_Don't_Save":
        print("Exit_Don't_Save is function to Don't save and exit the edits to use you should write:\n Exit_Don't_Save")

    elif command == "Edit_Don't_Save":
        print("Edit_Don't_Save is function to Don't save the edits to use you should write:\n Edit_Don't_Save|")

    elif command == "Edit_Save":
        print("Edit_Save is function to to save edits in middle of progress to use you should write:\n Edit_Save|")

    
    else:
        print("Wrong Command inputed!\n if you don't know how to use this app just write:\n Help| or Help|name_of_a_command")
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
def Show (imagename):
    try:
        img = Image.open(imagename)
        
    except IOError:
        print("Unable to load image")    
        sys.exit(1)
    img.show()
    
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
        realimagename = command[1]
        print("command Ended write Another:\n")
    elif command[0] == "Rotate"and len(command)==2 and imagename != "" and imagename != "Unable to load image":
        Rotate(imagename,-(int(command[1])))
        print("command Ended write Another:\n")
    elif command[0] == "Crop"and len(command)==2 and imagename != "" and imagename != "Unable to load image":
        Values = command[1].split(",")
        if len(Values)==4:
            Crop(imagename,int(Values[0]),int(Values[1]),int(Values[2]),int(Values[3]))
            print("command Ended write Another:\n")
        
    elif command[0] == "WaterMark"and len(command)==2 and imagename != "" and imagename != "Unable to load image":
        Values = command[1].split(",")
        if len(Values)==5:
            WaterMark(imagename,Values[0],int(Values[1]),Values[2],int(Values[3]),int(Values[4]))
            print("command Ended write Another:\n")
        else:
            print("Wrong input goto Help|WaterMark")
        
    elif command[0] == "Help"and len(command)==2:
        if command[1] == " " or command[1] == '':
            print ("OK lets start this app built to help you with editing a photo \n\n to command you should write: \n Command|values \n\n Command: is name of the command that you want to do like Blur, Rotate,... \n | : you shoud put this between command and values \n value : is the inputs of the functions that you use \n\nto start editing write:\n Open|image_name\n\nlist of commands:\nBlur|\nGrayScale|\nRotate|value1\nShow|\nWaterMark|fontname,fontsize,text,x,y\nCrop|x1,y1,x2,y2\nEdit_Save|\nEdit_Don't_Save|\nExit_Save\nExit_Don't_Save\n\nTHANKS FOR USE ME")
        else:
            Help(command[1])
        print("command Ended write Another:\n")
    elif command[0] == "Undo_all"and len(command)==2 :
        Open(realimagename)
        print("command Ended write Another:\n")
    elif command[0] == "Show"and len(command)==2 :
        print("pleas close the image after you see it to continue")
        Show(imagename)
        print("command Ended write Another:\n")
    elif command[0] == "Edit_Don't_Save"and len(command)==2 :
        Show(imagename)
        print("command Ended write Another:\n")
    elif command[0] == "Edit_Save"and len(command)==2 :
        image_Save(imagename,realimagename)
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









