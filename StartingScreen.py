import pygame
import sys
from pygame.locals import *
import Weltkarte
from resources import Farben


class clsStartScreen(object):
    def __init__(self, screen, MODE, Status):
        self.screen = screen
        self.MODE = MODE
        self.Status = Status

    def draw(self, screen):
        INVENTARFONT = pygame.font.Font('./resources/fonts/customfont.ttf', 19)
        background = pygame.Rect(Weltkarte.MAPWIDTH*Weltkarte.TILESIZE,
                                 Weltkarte.MAPHEIGHT*Weltkarte.TILESIZE+50, 400, 400)

        if self.Status:
            returnbutton = pygame.Rect(100, 100, 80, 20)
            returnbuttonlabel = INVENTARFONT.render(
                "Weiter", 1, Farben.clsFarben.WHITE)
            pygame.draw.rect(
                self.screen, Farben.clsFarben.DARKRED, returnbutton)
            self.screen.blit(returnbuttonlabel, (100, 100))

            savebutton = pygame.Rect(100, 200, 80, 20)
            savebuttonlabel = INVENTARFONT.render(
                "Speichern", 1, Farben.clsFarben.WHITE)
            pygame.draw.rect(self.screen, Farben.clsFarben.DARKRED, savebutton)
            self.screen.blit(savebuttonlabel, (100, 200))
        else:
            newgamebutton = pygame.Rect(100, 100, 80, 20)
            newgamebuttonlabel = INVENTARFONT.render(
                "Neues Spiel", 1, Farben.clsFarben.WHITE)
            pygame.draw.rect(
                self.screen, Farben.clsFarben.DARKRED, newgamebutton)
            self.screen.blit(newgamebuttonlabel, (100, 100))

        loadbutton = pygame.Rect(200, 100, 80, 20)
        loadbuttonlabel = INVENTARFONT.render(
            "Laden", 1, Farben.clsFarben.WHITE)

        pygame.draw.rect(self.screen, Farben.clsFarben.WHITE, background)
        pygame.draw.rect(self.screen, Farben.clsFarben.DARKRED, loadbutton)
        self.screen.blit(loadbuttonlabel, (200, 100))

#    def decideMode(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                mousepos = event.pos
                if self.Status:
                    if returnbutton.collidepoint(mousepos):
                        self.MODE = "GAME"
                    elif savebutton.collidepoint(mousepos):
                        self.MODE = "SAVE"
                    elif loadbutton.collidepoint(mousepos):
                        self.MODE = "LOAD"
                    else:
                        self.MODE = "STARTSCREEN"
                else:
                    if newgamebutton.collidepoint(mousepos):
                        self.MODE = "NEWGAME"
                    elif loadbutton.collidepoint(mousepos):
                        self.MODE = "LOAD"
                    else:
                        self.MODE = "STARTSCREEN"

    def whichMode(self):
        return self.MODE
