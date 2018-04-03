import pygame, sys
from pygame.locals import *
import Weltkarte
import Farben

class clsStartScreen(object):
    def __init__(self, screen, MODE):
        self.screen=screen
        self.MODE=MODE

    def draw(self, screen):
        background=pygame.Rect(Weltkarte.MAPWIDTH*Weltkarte.TILESIZE, Weltkarte.MAPHEIGHT*Weltkarte.TILESIZE+50, 400,400)
        newgamebutton=pygame.Rect(100,100,80,20)
        savebutton = pygame.Rect(100,200,80,20)
        loadbutton = pygame.Rect(200,100, 80,20)

        pygame.draw.rect(self.screen, Farben.clsFarben.WHITE, background)
        pygame.draw.rect(self.screen, Farben.clsFarben.DARKRED, newgamebutton)
        pygame.draw.rect(self.screen, Farben.clsFarben.DARKRED, savebutton)
        pygame.draw.rect(self.screen, Farben.clsFarben.DARKRED, loadbutton)

#    def decideMode(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type==MOUSEBUTTONDOWN:
                mousepos=event.pos
                if savebutton.collidepoint(mousepos):
                    self.MODE="SAVE"
                elif loadbutton.collidepoint(mousepos):
                    self.MODE="LOAD"
                elif newgamebutton.collidepoint(mousepos):
                    self.MODE="NEWGAME"
                else:
                    self.MODE="UNKNOWN"
                return self.MODE