# PIL tutorial:

# Using the image class:
# 'Image' is one of the most important class.
from PIL import Image, ImageFilter, ImageEnhance, ImageSequence

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

# ====================================================
# Cutting, pasting and merging images.
# The Image class containing methods allowing you to manipulate regions
# within an image. To extract a sub-rectangle from an image, use the crop() method.
img = Image.open('sample.jpg')
box = (300, 300, 700, 700)
region = img.crop(box)
# region.save('cut.jpg')
# Image.open('cut.jpg').show()

# The region could now be processed in certain manner and pasted back.
region = region.transpose(Image.ROTATE_180)
img.paste(region, box)
# When pasting region back, the size of region must match the given region exactly.
# the region cannot extend outside the image. However the mode of original image and
# region do not need to match.
img.save('rotate_region.jpg')
# ====================================================

# Rolling an image
def roll(image, delta):
    xsize, ysize = image.size
    delta = delta % xsize
    if delta == 0: return image

    part1 = image.crop((0, 0, delta, ysize))
    part2 = image.crop((delta, 0, xsize, ysize))
    image.paste(part1, (xsize-delta, 0, xsize, ysize))
    image.paste(part2, (0, 0, xsize-delta, ysize))

    return image

img = Image.open('sample.jpg')
img = roll(img, 1000)
# img.show()
# ======================================================

# Splitting and merging bands
img = Image.open('sample.jpg')
r, g, b = img.split()
# The python Image library also allows you to work with the individual
# bands of an multi-band image, such as RGB image. The split method crates
# a set of new images, each containing one band from the original multi-band image.
img = Image.merge('RGB', (g, b, r))
# r.show()
# b.show()
# g.show()
# img.show()
# ======================================================

# Geometrical transforms
# The PIL.Image.Image class contains methods to resize() and rotate() an image.

# simple geometry transforms
img = Image.open('sample.jpg')
out_1 = img.resize((512, 256))
out_2 = img.rotate(45)
# out_1.show()
# out_2.show()

# transposing an image
out1 = img.transpose(Image.FLIP_LEFT_RIGHT)
out2 = img.transpose(Image.FLIP_TOP_BOTTOM)
out3 = img.transpose(Image.ROTATE_90)
out4 = img.transpose(Image.ROTATE_180)
out5 = img.transpose(Image.ROTATE_270)

# out1.show()
# out2.show()
# out3.show()
# out4.show()
# out5.show()
# ======================================================

# Color Transforms
# The python imageing library allows you to convert images between different pixel
# representation using convert() method.

img = Image.open('sample.jpg').convert('L')
img = Image.open('sample.jpg').convert('P')
img = Image.open('sample.jpg').convert('CMYK')
# https://pillow.readthedocs.io/en/3.1.x/reference/Image.html
# https://pillow.readthedocs.io/en/3.1.x/handbook/concepts.html#concept-modes
# img.show()
# ========================================================

# Image Enhancements - The python Imaging Library provides a number
# of methods and modules that can be used to enhance images

# Filters - The ImageFilter module contains a number of pre-defined
# enhancement filters that can be used with the filter() method
img = Image.open('sample.jpg')
out = img.filter(ImageFilter.DETAIL)
# out.show()

# Applying point transforms
# https://pillow.readthedocs.io/en/stable/handbook/tutorial.html
# https://pillow.readthedocs.io/en/3.1.x/reference/Image.html
# https://pillow.readthedocs.io/en/3.1.x/handbook/concepts.html#concept-modes

img = Image.open('sample.jpg')
# multiply each pixel by 12
out = img.point(lambda i: i * 12)
# out.show()
# using the above technique, you can quickly apply any simple expression to an image.
# you can also combine the point() and paste() methods to selectively modify an image.

# processing individual bands
img = Image.open('sample.jpg')
R, G, B = img.split()
# Select region where red is less than 100
RR = R.point(lambda i: i < 100 and 255)
# process the green band
GG = G.point(lambda i: i * 0.7)
# paste the processed band back, but only where red was < 100
G.paste(GG, None, RR)
# build the new multiband image
img = Image.merge('RGB', (R,G,B))
# img.show()
# syntax used to create mask is:
# img = img.out(lambda i: expression and 255)
# ========================================================

# Enhancing images - Enhancement
# for more advanced image enhancement, you can use the classes in the ImageEnhance module.
# You can adjust contrast, brightness, color balance and sharpness in this way.

img = Image.open('sample.jpg')
enh = ImageEnhance.Contrast(img)
# img.show()
# enh.enhance(1.6).show()
# ========================================================

# Image sequences
# The PIL contains some basic support for image sequences (also called animation formats)
# Supported sequence formats include FLI/FLC, GIF and a few experimental formats. TIFF files can also contain more than one framesself.

img = Image.open('giphy.gif')
# img.show()
# img.seek(1) # skips the second frame
try:
    while True:
        img.seek(img.tell() + 1)
        # img.show()
except EOFError:
    pass

# Using image sequence iterator class.
for frame in ImageSequence.Iterator(img):
    # frame.show()
    frame
