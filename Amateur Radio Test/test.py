#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Richard
#
# Created:     28/12/2011
# Copyright:   (c) Richard 2011
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

def main():
    pass

if __name__ == '__main__':
    main()

##import easy_gui_test as eg
##import Tkinter as tk
##import PIL
####image   = "figure 1.gif"
##msg     = "Do you like this picture?"
##choices = ["Yes","No","No opinion"]
###reply   = eg.buttonbox(msg,image=image,choices=choices)
##
##eg.ynbox("hello", "title", image=image)
##eg.choicebox(msg,"hi",choices,image=image)
##photo = tk.PhotoImage(file="figure 1.gif")
##label = tk.Label(image=photo)
##label.image = photo # keep a reference!
##label.pack()
##photo

import Image
im = Image.open("figure 1.gif")
print im.format, im.size, im.mode
im.show()