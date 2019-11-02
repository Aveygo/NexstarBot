# Takes over and aligns the current picture by
# finding the brightest spot and moving untill its
# aligned. Radius (in function alignImage) defines 
# how blurred the image will be. MUST BE ODD.
# Too high and no details can be made out, too low
# and the wrong star might be found.  

import numpy as np
import argparse
import cv2

def alignImage(imagepath, radius=21): #returns relative to center
    image = cv2.imread(imagepath)
    height, width, channels = image.shape
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (radius, radius), 0)
    (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(gray)
    center = (width/2, height/2)  
    offset = (center[0]-maxLoc[0], center[1]-maxLoc[1])
    return offset

print(alignImage('stars.jpg'))