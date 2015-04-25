from SimpleCV import Camera
#-------------------------------------------------------------------------------
# Name:        Hello World v3
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

# Initialize the camera
cam = Camera(0,{"width": 900, "height": 300})

# Capture and image and display it
img0 = cam.getImage()
img0.drawText("I am Camera ID 0", 100, 100)
img0.live()
exit()