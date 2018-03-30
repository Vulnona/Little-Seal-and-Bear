#http://usingpython.com/dl/StayAlive.py
import tkinter
import pygame
import sys
from pygame.locals import *
import Weltkarte

class Menu(object):
    def __init__(self, screen, inventar, charakter):
        self.screen=screen
        self.inventar=inventar
        self.charakter=charakter
    def draw(self, screen, charakter):
        BG = pygame.Rect(45, 75, 500, 500)
        exitbutton = pygame.Rect(480, 420, 80, 20)
        INVENTARFONT = pygame.font.Font('customfont.ttf', 18)
        label = INVENTARFONT.render("Zurück", 1, (0, 0, 0))
        proceed = True
        while proceed:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == MOUSEBUTTONDOWN:
                    mousepos = event.pos
                    if exitbutton.collidepoint(mousepos):
                        proceed=False
                else:
                    pygame.draw.rect(self.screen, (0, 0, 0), BG)
                    pygame.draw.rect(self.screen, [255, 0, 0], exitbutton)
                    self.screen.blit(label, (495, 420))
                    actuallevel=INVENTARFONT.render("Level: " + str(charakter.getlevel()), 1, (255, 255, 255))
                    self.screen.blit(actuallevel,(100,100))
                    placePosition = 50
                    for item in Weltkarte.collectableres:
                        self.screen.blit(Weltkarte.snippets[item],
                                     (placePosition, Weltkarte.MAPHEIGHT * Weltkarte.TILESIZE + 20))
                        placePosition += 30
                        textObjekt = INVENTARFONT.render(str(Weltkarte.inventory[item]), True, (255,255,255),(0,0,0))
                        self.screen.blit(textObjekt, (placePosition, Weltkarte.MAPHEIGHT * Weltkarte.TILESIZE + 20))
                        placePosition += 50
                    if charakter.animaltype == "baer":
                        image = pygame.image.load('bearbig.png').convert()
                        image = pygame.transform.scale(image, (300,300))
                        self.screen.blit(image, (150,100))
                    else:
                        pass

                pygame.display.update()

        def interaktionen(self, inventar, charakter):
            pass

