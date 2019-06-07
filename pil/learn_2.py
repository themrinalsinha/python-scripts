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

# ====================================================
# controlling the decoder.
# Some decoders allow you to manipulate the image while reading it from a file. This can often be used to speed up
# decoding when creating thumbnails (when speed is usually more important thatn quality) and printing to a monochrome
# laser printer.
# The draft() method manipulates an opened but not yet loaded image so it as closely as possible matches the given mode and size.

# Reading in draft mode.
from PIL import Image
img = Image.open('sample.jpg')
print('original = ', img.mode, im.size)

img.draft('L', (100, 100))
print('draft = ', img.mode, img.size)
