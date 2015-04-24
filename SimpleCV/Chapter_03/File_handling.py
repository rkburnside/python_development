# -------------------------------------------------------------------------------
# Name: File Handling
# Purpose: learning SimpleCV
# Author:      Rich
# Created:     2015/03/14
# -------------------------------------------------------------------------------


def main():
    pass


if __name__ == '__main__':
    main()

from SimpleCV import Image

builtInImg = Image("logo")
webImg = Image(
    "http://i2.cdn.turner.com/cnnnext/dam/assets/140629184639-hernandez-surveillance-0617-horizontal-large-gallery.jpg")
localImg = Image("painting.png")
localImg.save("painting1.jpg")

exit()