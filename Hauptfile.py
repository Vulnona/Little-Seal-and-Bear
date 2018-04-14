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



#NewStartingScreen.draw(SURFACE)

def Spiel(MODE, Charakter):
    if MODE=="STARTSCREEN":
        SURFACE.fill(Farben.clsFarben.BLACK)
        print("In Bedingung Startscreen")
        #NewStartingScreen = StartingScreen.clsStartScreen(SURFACE, MODE)
        #while MODE=="STARTSCREEN":
        print("In Startscreen bedingung begin")

        INVENTARFONT = pygame.font.Font('customfont.ttf', 19)
        background = pygame.Rect(Weltkarte.MAPWIDTH * Weltkarte.TILESIZE,
                                 Weltkarte.MAPHEIGHT * Weltkarte.TILESIZE + 50, 400, 400)
        newgamebutton = pygame.Rect(100, 100, 80, 20)
        newgamebuttonlabel = INVENTARFONT.render("Neues Spiel", 1, Farben.clsFarben.WHITE)
        savebutton = pygame.Rect(100, 200, 80, 20)
        savebuttonlabel = INVENTARFONT.render("Speichern", 1, Farben.clsFarben.WHITE)
        loadbutton = pygame.Rect(200, 100, 80, 20)
        loadbuttonlabel = INVENTARFONT.render("Laden", 1, Farben.clsFarben.WHITE)

        pygame.draw.rect(SURFACE, Farben.clsFarben.WHITE, background)
        pygame.draw.rect(SURFACE, Farben.clsFarben.DARKRED, newgamebutton)
        pygame.draw.rect(SURFACE, Farben.clsFarben.DARKRED, savebutton)
        pygame.draw.rect(SURFACE, Farben.clsFarben.DARKRED, loadbutton)
        SURFACE.blit(newgamebuttonlabel, (100, 100))
        SURFACE.blit(savebuttonlabel, (100, 200))
        SURFACE.blit(loadbuttonlabel, (200, 100))
        print("In startscreen middle")
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                mousepos = event.pos
                if savebutton.collidepoint(mousepos):
                    MODE = "SAVE"
                elif loadbutton.collidepoint(mousepos):
                    MODE = "LOAD"
                elif newgamebutton.collidepoint(mousepos):
                    MODE = "NEWGAME"
                else:
                    MODE = "UNKNOWN"
                return MODE
        print("in startscreen bed end")

            #MODE = NewStartingScreen.draw(SURFACE)
            #if (MODE!="STARTSCREEN" and MODE!="UNKNOWN"):
            #    return Spiel(MODE,Charakter)
    elif MODE=="UNKNOWN":
        print(MODE)
        MODE="STARTSCREEN"
        #return Spiel(NEWMODE,Charakter)
        print(MODE)
        return MODE
        # debugging
        #Spiel(MODE, Charakter)
        #Spiel(object, MODE)

    elif MODE=="SAVE":
        #SURFACE.fill(Farben.clsFarben.BLACK)
        with open('savefile.dat', 'wb') as f:
            pickle.dump([Charakter], f, protocol=2)
        MODE="GAME"
        return Spiel(MODE,Charakter)
        #Spiel(object, MODE)

    elif MODE=="LOAD":
        #SURFACE.fill(Farben.clsFarben.BLACK)
        with open('savefile.dat', 'rb') as f:
            Baer1 = pickle.load(f)
        MODE="GAME"
        return Spiel(MODE,Charakter)
        #Spiel(object, MODE)

    elif MODE=="NEWGAME":
        SURFACE.fill(Farben.clsFarben.BLACK)
        for row in range(Weltkarte.MAPHEIGHT):
            for column in range(Weltkarte.MAPWIDTH):
                #pygame.draw.rect(SURFACE, Weltkarte.colours[Weltkarte.titlemap[row][column]], (column*Weltkarte.TILESIZE, row*Weltkarte.TILESIZE, Weltkarte.TILESIZE, Weltkarte.TILESIZE))
                SURFACE.blit(Weltkarte.textures[Weltkarte.tilemap[row][column]], (column*Weltkarte.TILESIZE, row*Weltkarte.TILESIZE))
                pygame.draw.rect(SURFACE, Farben.clsFarben.BLACK, blackbar)
        SURFACE.blit(CharakterForm.CHARACTER,(CharakterForm.POSITION[0]*Weltkarte.TILESIZE,CharakterForm.POSITION[1]*Weltkarte.TILESIZE))
        placePosition=50
        INVENTARFONT = pygame.font.Font('customfont.ttf', 19)
        for item in Weltkarte.collectableres:
            SURFACE.blit(Weltkarte.snippets[item],(placePosition,Weltkarte.MAPHEIGHT*Weltkarte.TILESIZE+20))
            placePosition+=30
            textObjekt=INVENTARFONT.render(str(Weltkarte.inventory[item]),True,Farben.clsFarben.WHITE,Farben.clsFarben.BLACK)
            SURFACE.blit(textObjekt,(placePosition, Weltkarte.MAPHEIGHT * Weltkarte.TILESIZE + 20))
            placePosition+=50

        pygame.draw.rect(SURFACE, Farben.clsFarben.DARKRED, interagierenbutton)
        label = INVENTARFONT.render("Charakter", 1, Farben.clsFarben.WHITE)
        SURFACE.blit(label, (Koordinaten.clsKoordinaten.CHARSHEETPOSX, Koordinaten.clsKoordinaten.CHARSHEETPOSY))
        MODE="GAME"
        return Spiel(MODE, Charakter)
        #Spiel(object, MODE)

    elif MODE=="GAME":
        #while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                mousepos = event.pos
                if interagierenbutton.collidepoint(mousepos):
                    Charaktermenu = Interaktion.Menu(SURFACE, Baer1)
                    Charaktermenu.draw(SURFACE, Baer1)

            elif event.type == KEYDOWN:
                if (event.key == K_ESCAPE):
                    MODE="STARTSCREEN"
                    return MODE
                if (event.key == K_RIGHT and CharakterForm.POSITION[0] < Weltkarte.MAPWIDTH - 1):
                    CharakterForm.POSITION[0] += 1
                if (event.key == K_LEFT and CharakterForm.POSITION[0] > 0):
                    CharakterForm.POSITION[0] -= 1
                if (event.key == K_DOWN and CharakterForm.POSITION[1] < Weltkarte.MAPHEIGHT - 1):
                    CharakterForm.POSITION[1] += 1
                if (event.key == K_UP and CharakterForm.POSITION[1] > 0):
                    CharakterForm.POSITION[1] -= 1
                if (event.key == K_SPACE):
                    currentTile = Weltkarte.tilemap[CharakterForm.POSITION[1]][CharakterForm.POSITION[0]]
                    if (currentTile == Weltkarte.WATER or currentTile == Weltkarte.DIRT):
                        pass
                    else:
                        Weltkarte.inventory[currentTile] += 1
                        Weltkarte.tilemap[CharakterForm.POSITION[1]][CharakterForm.POSITION[0]] = Weltkarte.DIRT
                if (event.key == K_e):
                    # STAR = pygame.draw.lines(SURFACE, Farben.clsFarben.GOLD, 1, LevelupForm.Star, 3)
                    # SURFACE.blit(STAR, (CharakterForm.POSITION[0]*Weltkarte.TILESIZE,CharakterForm.POSITION[1]*Weltkarte.TILESIZE))
                    pygame.draw.rect(SURFACE, Farben.clsFarben.BLACK, STAR, 2)

            #else:
            #    SURFACE.fill(Farben.clsFarben.BLACK)
            #    MODE = NewStartingScreen.draw(SURFACE)

            pygame.display.update()
    #Spiel(object,MODE)

Baer1=CharakterWerte.Charakter("baer", 0)
#MODE = "UNKNOWN"
MODE="STARTSCREEN"
while True:
    MODE=Spiel(MODE, Baer1)
    #print(MODE)


