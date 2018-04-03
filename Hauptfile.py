# Robbie likes: https://medium.com/@yvanscher/making-a-game-ai-with-deep-learning-963bb549b3d5

import pygame, sys
from pygame.locals import *
import pickle
import StartingScreen
import Weltkarte
import CharakterForm
import CharakterWerte
import Interaktion
#import LevelupForm
import Farben
import Koordinaten

SCHRIFTGROESSE = 19


pygame.init()
SURFACE=pygame.display.set_mode((Weltkarte.MAPWIDTH*Weltkarte.TILESIZE, Weltkarte.MAPHEIGHT*Weltkarte.TILESIZE+50))
INVENTARFONT=pygame.font.Font('customfont.ttf', SCHRIFTGROESSE)

pygame.display.set_caption("Bärenspiel")
blackbar=pygame.Rect(Koordinaten.clsKoordinaten.BLACKBARSTART, Koordinaten.clsKoordinaten.BLACKBAREND, Weltkarte.MAPWIDTH*Weltkarte.TILESIZE, Weltkarte.MAPHEIGHT * Weltkarte.TILESIZE)
interagierenbutton = pygame.Rect(Koordinaten.clsKoordinaten.BUTTONPOSX, Koordinaten.clsKoordinaten.BUTTONPOSY, Koordinaten.clsKoordinaten.BUTTONWIDTH, Koordinaten.clsKoordinaten.BUTTONHEIGTH)

Baer1=CharakterWerte.Charakter("baer", 0)
MODE = "UNKNOWN"
NewStartingScreen = StartingScreen.clsStartScreen(SURFACE,MODE)
#NewStartingScreen.draw(SURFACE)

while True:
    if MODE=="SAVE":
        SURFACE.fill(Farben.clsFarben.BLACK)
        with open('savefile.dat', 'wb') as f:
            pickle.dump([Baer1], f, protocol=2)
    elif MODE=="LOAD":
        SURFACE.fill(Farben.clsFarben.BLACK)
        with open('savefile.dat', 'rb') as f:
            Baer1 = pickle.load(f)
    elif MODE=="NEWGAME":
        SURFACE.fill(Farben.clsFarben.BLACK)
        for row in range(Weltkarte.MAPHEIGHT):
            for column in range(Weltkarte.MAPWIDTH):
                #pygame.draw.rect(SURFACE, Weltkarte.colours[Weltkarte.titlemap[row][column]], (column*Weltkarte.TILESIZE, row*Weltkarte.TILESIZE, Weltkarte.TILESIZE, Weltkarte.TILESIZE))
                SURFACE.blit(Weltkarte.textures[Weltkarte.tilemap[row][column]], (column*Weltkarte.TILESIZE, row*Weltkarte.TILESIZE))
                pygame.draw.rect(SURFACE, Farben.clsFarben.BLACK, blackbar)
        SURFACE.blit(CharakterForm.CHARACTER,(CharakterForm.POSITION[0]*Weltkarte.TILESIZE,CharakterForm.POSITION[1]*Weltkarte.TILESIZE))
        placePosition=50
        for item in Weltkarte.collectableres:
            SURFACE.blit(Weltkarte.snippets[item],(placePosition,Weltkarte.MAPHEIGHT*Weltkarte.TILESIZE+20))
            placePosition+=30
            textObjekt=INVENTARFONT.render(str(Weltkarte.inventory[item]),True,Farben.clsFarben.WHITE,Farben.clsFarben.BLACK)
            SURFACE.blit(textObjekt,(placePosition, Weltkarte.MAPHEIGHT * Weltkarte.TILESIZE + 20))
            placePosition+=50

        pygame.draw.rect(SURFACE, Farben.clsFarben.DARKRED, interagierenbutton)
        label = INVENTARFONT.render("Charakter", 1, Farben.clsFarben.WHITE)
        SURFACE.blit(label, (Koordinaten.clsKoordinaten.CHARSHEETPOSX, Koordinaten.clsKoordinaten.CHARSHEETPOSY))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type==MOUSEBUTTONDOWN:
                mousepos=event.pos
                if interagierenbutton.collidepoint(mousepos):
                    Charaktermenu=Interaktion.Menu(SURFACE, Baer1)
                    Charaktermenu.draw(SURFACE, Baer1)

            elif event.type==KEYDOWN:
                if(event.key==K_ESCAPE):
                    MODE="STARTMENU"
                if(event.key==K_RIGHT and CharakterForm.POSITION[0]<Weltkarte.MAPWIDTH-1):
                    CharakterForm.POSITION[0]+=1
                if(event.key==K_LEFT and CharakterForm.POSITION[0]>0):
                    CharakterForm.POSITION[0]-=1
                if(event.key==K_DOWN and CharakterForm.POSITION[1]<Weltkarte.MAPHEIGHT-1):
                    CharakterForm.POSITION[1]+=1
                if(event.key==K_UP and CharakterForm.POSITION[1]>0):
                    CharakterForm.POSITION[1]-=1
                if(event.key==K_SPACE):
                    currentTile=Weltkarte.tilemap[CharakterForm.POSITION[1]][CharakterForm.POSITION[0]]
                    if(currentTile==Weltkarte.WATER or currentTile==Weltkarte.DIRT):
                        pass
                    else:
                        Weltkarte.inventory[currentTile]+=1
                        Weltkarte.tilemap[CharakterForm.POSITION[1]][CharakterForm.POSITION[0]]=Weltkarte.DIRT
                if(event.key==K_e):
                    #STAR = pygame.draw.lines(SURFACE, Farben.clsFarben.GOLD, 1, LevelupForm.Star, 3)
                    #SURFACE.blit(STAR, (CharakterForm.POSITION[0]*Weltkarte.TILESIZE,CharakterForm.POSITION[1]*Weltkarte.TILESIZE))
                    pygame.draw.rect(SURFACE, Farben.clsFarben.BLACK, STAR, 2)
    else:
        SURFACE.fill(Farben.clsFarben.BLACK)
        MODE = NewStartingScreen.draw(SURFACE)
        pygame.display.update()
    pygame.display.update()
