from PIL import Image, ImageOps
import numpy
import sys

def makeclear(inputimg):
    datas = inputimg.getdata()
    newData = []
    for item in datas:
        if item[0] == 255 and item[1] == 255 and item[2] == 255:
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)
    inputimg.putdata(newData)
    return inputimg

def generate_cypher_block(images, keys):
    maskimg1 = Image.open(images[0])
    maskimg2 = Image.open(images[1])
    maskimg3 = Image.open(images[2])
    key_red = Image.open(keys[0])
    key_green = Image.open(keys[1])
    key_blue = Image.open(keys[2])
    imageData = numpy.zeros((450,800,3),dtype=numpy.uint8)
    for x in range(450):
      for y in range(800):
        temp = list(maskimg1.getpixel((y,x)))
        if (temp[0] > 135 or temp[1] > 135 or temp[2] > 135 ):
          red = key_red.getpixel((y,x))[3]
        else:
          red = 255 - key_red.getpixel((y,x))[3]
        temp = list(maskimg2.getpixel((y,x)))
        if (temp[0] > 135 or temp[1] > 135 or temp[2] > 135):
          green = key_green.getpixel((y,x))[3]
        else:
          green = 255 - key_green.getpixel((y,x))[3]
        temp = list(maskimg3.getpixel((y,x)))
        if (temp[0] > 135 or temp[1] > 135 or temp[2] > 135 ):
          blue = key_blue.getpixel((y,x))[3]
        else:
          blue = 255 - key_blue.getpixel((y,x))[3]
        imageData[x,y] = [red,green,blue]
    cypher = Image.fromarray(imageData, mode="RGB")
    return cypher

cypher = generate_cypher_block(sys.argv[1].split(','), sys.argv[2].split(','))
cypher.save("CypherImage.png")
