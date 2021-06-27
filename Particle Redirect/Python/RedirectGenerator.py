# Max van Leeuwen
# maxvanleeuwen.com
# twitter.com/maksvanleeuwen
#
#
# Opens a png, saves redirection map as new png.
# For use with Particle Redirect Sub-Gaph in Lens Studio's VFX Editor.
# Use on low res images!
#
#
# Needs Python3, PIL.
#
# python3 <this py path> <png path>
# 	example: python3 ./RedirectGenerator.py ./ExampleSpawnMap.png



import math
import random
import sys
import PIL
from PIL import Image



# get png path
imgPath = sys.argv[1]
removeFromNameLength = '.png'
pathNoExt = imgPath[:-len(removeFromNameLength)]


# get png data
img = Image.open(imgPath)
imgRed = img.getchannel('R')
width, height = img.size


# texture width
outWidth = 2048



# function to remap 0-width to 0-255
def remap(v):
	return round((v/width) * 255)



pixCount = 0
lastPercentage = 0
maxPixCount = width * height
def updatePixelPercentage():
	global pixCount
	global lastPercentage
	global maxPixCount

	pixCount += 1
	percentage = round(100*(pixCount/maxPixCount))
	if(percentage != lastPercentage):
		print( str(percentage) + "%")
		lastPercentage = percentage



def generateImage():
	# go through each row in image, search for lines with start and end positions
	areas = []
	for y in range(height):
		start = -1
		for x in range(width):
			r = imgRed.getpixel((x, y))
			if r > .5:
				if start == -1:
					start = x
			else:
				if start != -1:
					areas.append([start, x, y])
					start = -1

			updatePixelPercentage()

	print("writing image...")

	# make image with area data
	pixelCount = len(areas)
	outHeight = math.ceil(pixelCount/outWidth)
	leftoverWidth = outWidth - round((pixelCount/outWidth - math.floor(pixelCount/outWidth)) * outWidth)
	
	out = Image.new('RGB', (outWidth, outHeight))
	for i in range(pixelCount):
		area = areas[i]
		outX = i%outWidth
		outY = math.floor(i/outWidth)
		data = (remap(area[0]), remap(area[1]), remap(area[2]))
		out.putpixel((outX, outY), data)

	# fill leftover of texture with random areas from earlier
	for i in range(leftoverWidth):
		outX = outWidth-(leftoverWidth) + i
		outY = math.floor(pixelCount/outWidth)
		area = areas[math.floor(random.random()*pixelCount)]
		data = (remap(area[0]), remap(area[1]), remap(area[2]))
		out.putpixel((outX, outY), data)

	# save and display new image
	outPath = pathNoExt + "_redirect.png"
	out.save(outPath)

	print("done! saved to:")
	print(outPath)



generateImage()