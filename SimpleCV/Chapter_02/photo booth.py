#-------------------------------------------------------------------------------
# Name: Photo booth application
# Purpose: learning SimpleCV
# Author:      Rich
# Created:     2015/03/14
#-------------------------------------------------------------------------------


def main():
    pass

if __name__ == '__main__':
    main()

from SimpleCV import Camera, Display, Color
import time

# Initialize the Camera
cam = Camera()

# Initialize the display
display = Display()

# Take an initial picture
img = cam.getImage()

# Write a message on the image
img.drawText("Left click to save a photo.", color=Color().getRandom())

# Show the image on the display
img.save(display)

time.sleep(5)

counter = 0
while not display.isDone():
    # Update the display with the latest image
    img = cam.getImage()

    img.save(display)

    if display.mouseLeft:
        # Save image to the current directory
        img.save("photobooth" + str(counter) + ".jpg")

        img.drawText("Photo saved.", color=Color().getRandom())

        img.save(display)

        time.sleep(5)

        counter = counter + 1

    if display.mouseRight:
        exit()