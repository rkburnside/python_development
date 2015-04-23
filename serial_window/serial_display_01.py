import pygame

__author__ = 'Rich'


# initialize
pygame.init()
resolution = 400, 200
screen = pygame.display.set_mode(resolution)

# pygame.mouse.set_cursor(*pygame.cursors.diamond)

fg = 250, 240, 230
bg = 5, 5, 5
wincolor = 255, 255, 255

# fill background
screen.fill(wincolor)

# load font, prepare values
font = pygame.font.Font(None, 80)
text = 'Fonty'
size = font.size(text)

# no AA, no transparancy, normal
ren = font.render(text, 0, fg, bg)
screen.blit(ren, (10, 10))