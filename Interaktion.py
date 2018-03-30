#http://usingpython.com/dl/StayAlive.py
import tkinter
import pygame
import sys
from pygame.locals import *
import Farben
import Weltkarte

class Menu(object):
    def __init__(self, screen, charakter):
        self.screen=screen
        self.charakter=charakter
    def interaktionen(self, charakter):
        INVENTARFONT = pygame.font.Font('customfont.ttf', 19)
        proceed=True
        while proceed:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                else:
                    label = INVENTARFONT.render("Craftables: ", 0, Farben.clsFarben.WHITE)
                    exitbutton = pygame.Rect(480, 420, 80, 20)
                    pygame.draw.rect(self.screen, Farben.clsFarben.DARKRED, exitbutton)
                    self.screen.blit(label, (100, 125))
                    placePosition=150
                    for item in Weltkarte.allcraftables:
                        self.screen.blit(Weltkarte.crafts[item],(120, placePosition))
                        placePosition += 60
                        textObjekt = INVENTARFONT.render(str(Weltkarte.inventorycrafts.get(item)), True, Farben.clsFarben.WHITE,Farben.clsFarben.BLACK)
                        self.screen.blit(textObjekt, (100, placePosition-40))
                        placePosition += 40
                    if event.type == MOUSEBUTTONDOWN:
                        mousepos = event.pos
                        if exitbutton.collidepoint(mousepos):
                            proceed = False
                pygame.display.update()

    def draw(self, screen, charakter):
        # Rect(left, top, width, height)
        buttonwidth = 80
        buttonheigth = 20
        INVENTARFONT = pygame.font.Font('customfont.ttf', 19)
        BG = pygame.Rect(45, 75, 500, 500)
        exitbutton = pygame.Rect(480, 420, buttonwidth, buttonheigth)
        feedbutton = pygame.Rect(280, 400, buttonwidth, buttonheigth)
        label = INVENTARFONT.render("Zurück", 1, Farben.clsFarben.WHITE)
        feedlabel= INVENTARFONT.render("Füttern", 1, Farben.clsFarben.WHITE)
        proceed = True
        while proceed:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                else:
                    pygame.draw.rect(self.screen, Farben.clsFarben.BLACK, BG)
                    pygame.draw.rect(self.screen, Farben.clsFarben.DARKRED, exitbutton)
                    self.screen.blit(label, (495, 420))
                    actuallevel=INVENTARFONT.render("Level: " + str(charakter.getlevel()), 1, (255, 255, 255))
                    self.screen.blit(actuallevel,(100,100))
                    pygame.draw.rect(self.screen, Farben.clsFarben.DARKRED, feedbutton)
                    self.screen.blit(feedlabel, (300, 400))
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

                    if event.type == MOUSEBUTTONDOWN:
                        mousepos = event.pos
                        if exitbutton.collidepoint(mousepos):
                            proceed = False
                        if feedbutton.collidepoint(mousepos):
                            self.interaktionen(charakter)

                pygame.display.update()


