from PIL import Image
import glob

height = 100000

for filename in glob.glob('/home/deeplearning/Pictures/*'):
    im = Image.open(filename)
    tmp_width, tmp_height = im.size

    if tmp_height < height:
        width, height = im.size

for filename in glob.glob('/home/deeplearning/Pictures/*'):
    im = Image.open(filename)
    im.thumbnail([height,height], Image.ANTIALIAS)


