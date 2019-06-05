# PIL tutorial:

# Using the image class:
# 'Image' is one of the most important class.
from PIL import Image

# To load an image from a file, use the open() function in the Image module.
img = Image.open('sample.jpg')
print(img.format, img.size, img.mode)
# format - attribute identifies sourceself
# size - attribute is a 2-tuple containing width and height in pixels
# mode - attribute show mode like L for greyscale, RGB for truecolor, CMYK for pre-press image

# Once u have instance of the Image class, you can use the methods defines by this class
# to process and manipulate the image.

# To display image.
# img.show()
# ====================================================

# Reading and writing image
# To save a file, use the save() method of the Image class. When saving files,
# the name becomes important. Unless you specify the format, the library uses the filename
# extension to discover which file storage format to use.

# convert files to JPEG
Image.open('sample.jpg').save('jpg_to_png.png')

# create JPEG thumbnails
size = (256, 256)
img  = Image.open('sample.jpg')
img.thumbnail(size)
img.save('icon.thumbnail', "JPEG")
