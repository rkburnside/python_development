#-------------------------------------------------------------------------------
# Name:        Hello World v2
# Purpose: learning SimpleCV
#
# Author:      Rich
#
# Created:     2015/03/13
# Copyright:   (c) Rich 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

from SimpleCV import Camera, Display
import time

# Initialize the camera
cam = Camera()

# Initialize the display
display = Display()

# Snap a picture using the camera
img = cam.getImage()

time.sleep(3)
# Show some text
img.drawText("Hello World")

# Show the picture on the screen
img.save(display)

# Wait five seconds so the window doesn't close right away
time.sleep(5)