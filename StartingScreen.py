import pygame, sys
from pygame.locals import *
import Weltkarte
from resources import Farben


class clsStartScreen(object):
    def __init__(self, screen, MODE):
        self.screen=screen
        self.MODE=MODE

    def draw(self, screen):
        INVENTARFONT = pygame.font.Font('./resources/fonts/customfont.ttf', 19)
        background=pygame.Rect(Weltkarte.MAPWIDTH*Weltkarte.TILESIZE, Weltkarte.MAPHEIGHT*Weltkarte.TILESIZE+50, 400,400)
        newgamebutton=pygame.Rect(100,100,80,20)
        newgamebuttonlabel=INVENTARFONT.render("Neues Spiel", 1, Farben.clsFarben.WHITE)
        savebutton = pygame.Rect(100,200,80,20)
        savebuttonlabel=INVENTARFONT.render("Speichern", 1, Farben.clsFarben.WHITE)
        loadbutton = pygame.Rect(200,100, 80,20)
        loadbuttonlabel=INVENTARFONT.render("Laden", 1, Farben.clsFarben.WHITE)

        pygame.draw.rect(self.screen, Farben.clsFarben.WHITE, background)
        pygame.draw.rect(self.screen, Farben.clsFarben.DARKRED, newgamebutton)
        pygame.draw.rect(self.screen, Farben.clsFarben.DARKRED, savebutton)
        pygame.draw.rect(self.screen, Farben.clsFarben.DARKRED, loadbutton)
        self.screen.blit(newgamebuttonlabel, (100,100))
        self.screen.blit(savebuttonlabel, (100,200))
        self.screen.blit(loadbuttonlabel, (200,100))

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
                    self.MODE="STARTSCREEN"
                #return self.MODE

    def whichMode(self):
        return self.MODE