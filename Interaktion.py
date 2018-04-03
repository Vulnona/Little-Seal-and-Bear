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
                    craftbuttonx=100
                    craftbuttony=200
                    pygame.draw.rect(self.screen, Farben.clsFarben.DARKRED, exitbutton)
                    # pygame.draw.rect(self.screen, Farben.clsFarben.GOLD, craftbuttons[item])
                    self.screen.blit(label, (100, 125))

                    placePosition=150
                    for item in Weltkarte.craftables:
                        self.screen.blit(Weltkarte.craftsnippets[item],(120, placePosition))
                        placePosition += 60
                        textObjekt = INVENTARFONT.render(str(Weltkarte.inventorycrafts.get(item)), True, Farben.clsFarben.WHITE,Farben.clsFarben.BLACK)
                        self.screen.blit(textObjekt, (100, placePosition-40))
                        placePosition += 40
                        craftbutton = pygame.Rect(craftbuttonx, craftbuttony, 60, 15)
                        pygame.draw.rect(self.screen, Farben.clsFarben.BROWN, craftbutton)
                        craftlabel = INVENTARFONT.render("Herstellen", 0, Farben.clsFarben.GOLD)
                        self.screen.blit(craftlabel, (craftbuttonx + 5, craftbuttony - 1))
                        craftbuttony+=100
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
        #craftbutton1= pygame.Rect(90,200, buttonwidth, buttonheigth)
        #craftbutton2 = pygame.Rect(90, 240, buttonwidth, buttonheigth)
        #craftbutton3= pygame.Rect(90, 280, buttonwidth, buttonheigth)
        #craftbuttons={craftbutton1,craftbutton2,craftbutton3}
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
                        placePosition += 35
                    if charakter.animaltype == "baer":
                        if charakter.level<4:
                            image = pygame.image.load('babybear.png').convert()
                            image = pygame.transform.scale(image, (300, 300))
                            self.screen.blit(image, (200, 100))
                        elif charakter.level>=4 and charakter.level<=8:
                            image = pygame.image.load('bearbig.png').convert()
                            image = pygame.transform.scale(image, (300,300))
                            self.screen.blit(image, (200,100))
                        elif charakter.level>8:
                            image = pygame.image.load('bearfinallevel.png').convert()
                            image = pygame.transform.scale(image, (300, 300))
                            self.screen.blit(image, (200, 100))

                    else:
                        pass

                    if event.type == MOUSEBUTTONDOWN:
                        mousepos = event.pos
                        if exitbutton.collidepoint(mousepos):
                            proceed = False
                        if feedbutton.collidepoint(mousepos):
                            self.interaktionen(charakter)

                pygame.display.update()


