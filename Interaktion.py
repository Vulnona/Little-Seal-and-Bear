#http://usingpython.com/dl/StayAlive.py
import tkinter
import pygame
from pygame.locals import *

class Menu(object):
    def __init__(self, screen):
        self.screen=screen
    def draw(self, screen):
        BG = pygame.Rect(100, 100, 400, 400)
        pygame.draw.rect(self.screen, (0, 0, 0), BG, 2)
        #pygame.display.flip
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()