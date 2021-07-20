import pygame as py
from pygame.locals import *
from utils import Circles, randColor
import random
py.init()

# constants
disp_tuple = (1080, 720)
caption = 'Load animation'
SCREEN = py.display.set_mode(disp_tuple)
CAPTION = py.display.set_caption(caption)
running = True
#  circle variables
circle_list = []
for circle in range(10):
    x = SCREEN.get_width()/2
    y = SCREEN.get_height()/2
    dx, dy = 1, 1
    rad = random.randint(40, 80)
    stroke = 2
    color = randColor()
    i = Circles(x, y, dx, dy, rad, stroke, SCREEN, color)
    circle_list.append(i)


# main loop

if __name__ == '__main__':
    while running:
        SCREEN.fill((36, 36, 36))
        for event in py.event.get():
            if event.type == QUIT:
                running = False
        for i in circle_list:
            i.draw_circle()
        py.display.update()

py.quit()
