import pygame as py
import random
import math
rand_list = []
for i in range(20):
    i = random.randrange(50, 100)
    if i in rand_list:
        i = random.randrange(50, 100)
    else:
        rand_list.append(i)


def randColor():
    r, g, b = random.randrange(0, 255), random.randrange(
        0, 255), random.randrange(0, 255)
    return r, g, b


class Circles:
    def __init__(self, x, y, dx, dy, rad, stroke, screen, color):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.rad = rad
        self.stroke = stroke
        self.screen = screen
        self.color = color

    def draw_circle(self):
        py.draw.circle(self.screen, self.color,
                       (self.x, self.y), self.rad, self.stroke, True, False, True, False)
