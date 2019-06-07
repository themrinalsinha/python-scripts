from PIL import Image
from PIL import PSDraw
from PIL import TarIO, ContainerIO

im = Image.open("sample.jpg")
title = "hopper"
box = (1*72, 2*72, 7*72, 10*72) # in points

ps = PSDraw.PSDraw() # default is sys.stdout
ps.begin_document(title)

# draw the image (75 dpi)
ps.image(box, im, 75)
ps.rectangle(box)

# draw title
ps.setfont("HelveticaNarrow-Bold", 36)
ps.text((3*72, 4*72), title)

ps.end_document()
# im.show()
# ====================================================

# more on reading images

# As described earlier, the open() function of the Image module is used to open an image file. In most cases,
# you simply pass it the filename as an argument.

img = Image.open('sample.jpg')

with open('sample.jpg', 'rb') as fp:
    img = Image.open(fp)
    # img.show()

# you can use ContaineIO or TarIO module to access image file embedded in a larger file.
# Reading from a tar archive.
img = TarIO.TarIO('sample.tar', 'sample.jpg')
img = Image.open(img)
# img.show()
