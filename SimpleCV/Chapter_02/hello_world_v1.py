#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      Rich
#
# Created:     31/12/2014
# Copyright:   (c) Rich 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------


def main():
    pass

if __name__ == '__main__':
    main()

from SimpleCV import Camera, Display, Image
from time import sleep

# Initialize the camera
cam = Camera()

# Initialize the display
display = Display()

# Snap a picutre using the camera
sleep(5)
img = cam.getImage()
# Show the picture on the screen
img.save(display)
sleep(5)
exit()