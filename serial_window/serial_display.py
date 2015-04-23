__author__ = 'Rich'


# pygame draw
import serial
import pygame
import time
from pygame.locals import *
from sys import exit
from random import *

ser = serial.Serial(16, 115200, timeout=1000)
pygame.init()
SCREEN_DEFAULT_SIZE = (1000, 500)
SCREEN_DEFAULT_COLOR = (0, 0, 0)

screen = pygame.display.set_mode(SCREEN_DEFAULT_SIZE, 0, 32)
screen.fill(SCREEN_DEFAULT_COLOR)

# initialize font; must be called after 'pygame.init()' to avoid 'Font not Initialized' error
myfont_text = pygame.font.SysFont("monospace", 75)
myfont_numbers = pygame.font.SysFont("monospace", 200)


while 1:
    temp = ser.readline()
    temp = temp.strip()
    temp = temp.split(',')

    screen.fill(SCREEN_DEFAULT_COLOR)
    # for s in temp:
    #     s = s.split(',')
    #     pygame.draw.circle(screen, (250, 250, 250), (1024 - int(s[1]), 800 - int(s[2])), int(s[3]) * 10)
    screen.fill(SCREEN_DEFAULT_COLOR)
    time.sleep(.1)

    # render text
    label_IR = myfont_text.render("Infrared", 1, (255,255,0))
    screen.blit(label_IR, (15, 0))
    label_IR = myfont_text.render("Distance", 1, (255,255,0))
    screen.blit(label_IR, (15, 75))

    label_IR = myfont_numbers.render(str(temp[0]), 1, (255,255,0))
    screen.blit(label_IR, (35, 150))

    label_IR = myfont_text.render("Ultrasonic", 1, (255,255,0))
    screen.blit(label_IR, (500, 0))
    label_IR = myfont_text.render(" Distance", 1, (255,255,0))
    screen.blit(label_IR, (500, 75))

    label_sonic = myfont_numbers.render(str(temp[1]), 1, (255,255,0))
    screen.blit(label_sonic, (625, 150))

    pygame.display.update()
