# from SimpleCV import Image
#
# img = Image("logo")
#
# img.show(type="browser")

from SimpleCV import Display, Image
import time

display = Display()
Image("logo").save(display)
print "I launched a window"

while not display.isDone():
    time.sleep(0.1)

print "you closed the window"