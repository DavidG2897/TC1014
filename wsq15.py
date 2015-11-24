from PIL import Image

def work(image):
    im = Image.open(image)
    rot = int(input("Rotate 0, 90, 180 or 270 degrees? "))
    if (rot == 0):
        im = im.rotate(0)
    elif (rot == 90):
        im = im.rotate(90)
    elif(rot == 180):
        im = im.rotate(180)
    elif(rot == 270):
        im = im.rotate(270)
    flip = input("Flip horizontally or vertically or do nothing? (H or V or N) ")
    if(flip == "H"):
        im = im.transpose(Image.FLIP_LEFT_RIGHT)
    elif(flip == "V"):
        im = im.transpose(Image.FLIP_TOP_BOTTOM)
    resx = int(input("Give me the new size of x: "))
    resy = int(input("Give me the new sie of y: "))
    im = im.resize((resx,resy))
    im = im.save(image)
    return (im)

work(input("Give me the name of the image: "))
