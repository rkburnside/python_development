#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Richard
#
# Created:     02/03/2012
# Copyright:   (c) Richard 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

def main():
    pass

if __name__ == '__main__':
    main()

import cv

hc = cv.Load("c:\\facial_data\\haarcascade_frontalface_default.xml")
img = cv.LoadImage("c:\\facial_data\\IMG_0004.JPG", 0)
faces = cv.HaarDetectObjects(img, hc, cv.CreateMemStorage())
for (x,y,w,h),n in faces:
    cv.Rectangle(img, (x,y), (x+w,y+h), 255)
print faces
cv.SaveImage("c:\\facial_data\\faces_detected.jpg", img)