# -------------------------------------------------------------------------------
# Name: Time-Lapse Photography
# Purpose: learning SimpleCV
# Author:      Rich
# Created:     2015/03/13
# -------------------------------------------------------------------------------


def main():
    pass

if __name__ == '__main__':
    main()

from SimpleCV import Camera
import time

cam = Camera()

# Set the number of frames to capture
numFrames = 10

# Loop until we reach the limit set in numFrames
for x in range(0, numFrames):
    img = cam.getImage()

    filepath = "image-" + str(x) + ".jpg"
    img.save(filepath)
    print "Saved image to: " + filepath

    time.sleep(3)