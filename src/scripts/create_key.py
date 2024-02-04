from PIL import Image, ImageOps
import numpy

def gen_key(r,g,b, t):
    data = numpy.zeros((450,800,4),dtype=numpy.uint8)
    for x in range(450):
      for y in range(800):
        temp = numpy.random.random_sample()
        if temp < t:
          data[x,y] = [255*r,255*g,255*b,255]
        else:
          data[x,y] = [255,255,255,0]
    return Image.fromarray(data, mode="RGBA")

key_red = gen_key(1,0,0, .5)
key_red.save("key_red.png")
key_green = gen_key(0,1,0, .5)
key_green.save("key_green.png")
key_blue = gen_key(0,0,1, .5)
key_blue.save("key_blue.png")
