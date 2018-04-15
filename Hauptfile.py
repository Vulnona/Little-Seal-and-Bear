# Robbie likes: https://medium.com/@yvanscher/making-a-game-ai-with-deep-learning-963bb549b3d5
# Very nice: http://game-icons.net/

import pygame, sys
from pygame.locals import *
import pickle
import StartingScreen
import Weltkarte
import Interaktion
#import LevelupForm
from resources import Farben, Koordinaten
import game
import run
import character

SCHRIFTGROESSE = 19
INVENTARFONT = pygame.font.Font('./resources/fonts/customfont.ttf', SCHRIFTGROESSE)

pygame.init()
SURFACE=pygame.display.set_mode((Weltkarte.MAPWIDTH*Weltkarte.TILESIZE, Weltkarte.MAPHEIGHT*Weltkarte.TILESIZE+50))


pygame.display.set_caption("Bärenspiel")

blackbar=pygame.Rect(Koordinaten.clsKoordinaten.BLACKBARSTART, Koordinaten.clsKoordinaten.BLACKBAREND, Weltkarte.MAPWIDTH * Weltkarte.TILESIZE, Weltkarte.MAPHEIGHT * Weltkarte.TILESIZE)
interagierenbutton = pygame.Rect(Koordinaten.clsKoordinaten.BUTTONPOSX, Koordinaten.clsKoordinaten.BUTTONPOSY, Koordinaten.clsKoordinaten.BUTTONWIDTH, Koordinaten.clsKoordinaten.BUTTONHEIGTH)


def Spiel(MODE, Charakter):

    if MODE=="STARTSCREEN":
        NewStartingScreen = StartingScreen.clsStartScreen(SURFACE, MODE)
        NewStartingScreen.draw(SURFACE)
        pygame.display.update()
        MODE=NewStartingScreen.whichMode()
        return MODE

    elif MODE=="UNKNOWN":
        print(MODE)
        MODE="STARTSCREEN"
        print(MODE)
        return MODE

    elif MODE=="SAVE":
        with open('savefile.dat', 'wb') as f:
            pickle.dump([Charakter, Weltkarte.inventory], f, protocol=2)
            print(MODE)
        MODE="GAME"
        return MODE

    elif MODE=="LOAD":
        with open('savefile.dat', 'rb') as f:
            Charakter, Weltkarte.inventory = pickle.load(f)
        print(MODE)
        MODE="GAME"
        return MODE

    elif MODE=="NEWGAME":
        SURFACE.fill(Farben.clsFarben.BLACK)
        while True:
            run.run()

            startlabel = pygame.font.Font('customfont.ttf', SCHRIFTGROESSE+10).render("Such dir ein Tier aus... ", 0, Farben.clsFarben.WHITE)

            #NewGameScreen()
            pygame.display.update()

        MODE="GAME"
        return MODE
        #Spiel(object, MODE)

    elif MODE=="GAME":
        while True:
            pygame.display.update()

            for row in range(Weltkarte.MAPHEIGHT):
                for column in range(Weltkarte.MAPWIDTH):
                    SURFACE.blit(Weltkarte.textures[Weltkarte.tilemap[row][column]],
                                 (column * Weltkarte.TILESIZE, row * Weltkarte.TILESIZE))
                    pygame.draw.rect(SURFACE, Farben.clsFarben.BLACK, blackbar)

            SURFACE.blit(CharakterIcon.CHARACTER, (
                CharakterIcon.POSITION[0] * Weltkarte.TILESIZE, CharakterIcon.POSITION[1] * Weltkarte.TILESIZE))
            placePosition = 50

            for item in Weltkarte.collectableres:
                SURFACE.blit(Weltkarte.snippets[item], (placePosition, Weltkarte.MAPHEIGHT * Weltkarte.TILESIZE + 20))
                placePosition += 30
                textObjekt = INVENTARFONT.render(str(Weltkarte.inventory[item]), True, Farben.clsFarben.WHITE,
                                                 Farben.clsFarben.BLACK)
                SURFACE.blit(textObjekt, (placePosition, Weltkarte.MAPHEIGHT * Weltkarte.TILESIZE + 20))
                placePosition += 50

            pygame.draw.rect(SURFACE, Farben.clsFarben.DARKRED, interagierenbutton)
            label = INVENTARFONT.render("Charakter", 1, Farben.clsFarben.WHITE)
            SURFACE.blit(label, (Koordinaten.clsKoordinaten.CHARSHEETPOSX, Koordinaten.clsKoordinaten.CHARSHEETPOSY))


            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == MOUSEBUTTONDOWN:
                    mousepos = event.pos
                    if interagierenbutton.collidepoint(mousepos):
                        Charaktermenu = Interaktion.Menu(SURFACE, Charakter)
                        Charaktermenu.draw(SURFACE, Charakter)

                elif event.type == KEYDOWN:
                    if (event.key == K_ESCAPE):
                        MODE="STARTSCREEN"
                        return MODE
                    elif (event.key == K_RIGHT and CharakterIcon.POSITION[0] < Weltkarte.MAPWIDTH - 1):
                        CharakterIcon.POSITION[0] += 1
                    elif (event.key == K_LEFT and CharakterIcon.POSITION[0] > 0):
                        CharakterIcon.POSITION[0] -= 1
                    elif (event.key == K_DOWN and CharakterIcon.POSITION[1] < Weltkarte.MAPHEIGHT - 1):
                        CharakterIcon.POSITION[1] += 1
                    elif (event.key == K_UP and CharakterIcon.POSITION[1] > 0):
                        CharakterIcon.POSITION[1] -= 1
                    elif (event.key == K_SPACE):
                        currentTile = Weltkarte.tilemap[CharakterIcon.POSITION[1]][CharakterIcon.POSITION[0]]
                        if (currentTile == Weltkarte.WATER or currentTile == Weltkarte.DIRT):
                            pass
                        else:
                            Weltkarte.inventory[currentTile] += 1
                            Weltkarte.tilemap[CharakterIcon.POSITION[1]][CharakterIcon.POSITION[0]] = Weltkarte.DIRT
                    elif (event.key == K_e):
                        # STAR = pygame.draw.lines(SURFACE, Farben.clsFarben.GOLD, 1, LevelupForm.Star, 3)
                        # SURFACE.blit(STAR, (CharakterForm.POSITION[0]*Weltkarte.TILESIZE,CharakterForm.POSITION[1]*Weltkarte.TILESIZE))
                        pygame.draw.rect(SURFACE, Farben.clsFarben.BLACK, STAR, 2)

                    #else:
                    #    SURFACE.fill(Farben.clsFarben.BLACK)
                    #    MODE = NewStartingScreen.draw(SURFACE)

            #Spiel(object,MODE)

#Baer1= CharakterWerte.CharakterWerte("baer", 0)
#Baer1=CharakterWerte.CharakterWerte("Baer", "Weiss", 0)
Baer1=character.Character()
Baer1.create(name="Bruno",animaltype="Baer",animalsubtype="Schwarz",level=0)
MODE = "UNKNOWN"

while True:
    MODE=Spiel(MODE, Baer1)
    #print(MODE)


