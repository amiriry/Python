from PIL import Image
from sys import argv
from os import rename

filename=argv[1]
dot_position=filename.rfind('.')

print("choose image type you want(if not chosen, it will be png): ")
img_type = input()
if not img_type:
    img_type = "png"

newfilename=filename[0:dot_position] + "." + img_type
im = Image.open(filename)

resized=im.resize((1104,736))
resized.save(newfilename)
