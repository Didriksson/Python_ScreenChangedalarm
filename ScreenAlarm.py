import ImageGrab
import ImageOps
import os
import time
import Image
import winsound
from numpy import *

def screenGrab():
	im = ImageGrab.grab()
	return im

def greyscale(im1):
	im = ImageOps.grayscale(im1)
	return im
	
	
def compareImages(image,image2):
	imagedata = array(image.getcolors())
	imagedata2 = array(image2.getcolors())
	difference = 0
	for y in range(image.size[1]):
		for x in range(image.size[0]):
			if image.getpixel((x,y)) != image2.getpixel((x,y)):
				difference += 1
	
	percentage = (difference/float(image.size[0] * image.size[1])) * 100
	return percentage
	
def makeSomeNoice():
	winsound.Beep(300,2000)
	
def main():
	saveImages = False
	alarmActive = True
	while(1):
		time.sleep(2)
		previousImage = greyscale(screenGrab())
		time.sleep(5)
		currentImage = greyscale(screenGrab())
		difference = compareImages(previousImage, currentImage)
		if difference > 10:
			if saveImages:
				previousImage.save(os.getcwd() + '\\previousImage' + str(int(time.time())) + '.png', 'PNG')
				currentImage.save(os.getcwd() + '\\currentImage' + str(int(time.time())) + '.png', 'PNG')
			if alarmActive:
				makeSomeNoice()
		print difference
	
if __name__ == '__main__':
    main()