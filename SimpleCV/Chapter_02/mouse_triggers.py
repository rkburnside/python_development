from SimpleCV import Display, Image, Color

winsize = (640,480)
display = Display(winsize)

img = Image(winsize)
img.save(display)

while not display.isDone():
    if display.mouseLeft:
        img.dl().circle((display.mouseX, display.mouseY), 4, Color.YELLOW, filled=True)
        img.save(display)
        img.save("painting.png")
exit()