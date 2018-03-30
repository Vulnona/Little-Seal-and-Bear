import pygame, sys
from pygame.locals import *
import Weltkarte
import CharakterForm
import CharakterWerte
import Interaktion
import LevelupForm
import Farben


pygame.init()
SURFACE=pygame.display.set_mode((Weltkarte.MAPWIDTH*Weltkarte.TILESIZE, Weltkarte.MAPHEIGHT*Weltkarte.TILESIZE+50))
INVENTARFONT=pygame.font.Font('customfont.ttf',19)

pygame.display.set_caption("Bärenspiel")
blackbar=pygame.Rect(0,400,Weltkarte.MAPWIDTH*Weltkarte.TILESIZE,Weltkarte.MAPHEIGHT*Weltkarte.TILESIZE)
interagierenbutton = pygame.Rect(480, 420, 80, 20)

Baer1=CharakterWerte.Charakter("baer",0)

while True:
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
    SURFACE.blit(label, (495, 420))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type==MOUSEBUTTONDOWN:
            mousepos=event.pos
            if interagierenbutton.collidepoint(mousepos):
                #Interaktion.AgierenMenu(SURFACE,Weltkarte.MAPHEIGHT,Weltkarte.MAPWIDTH)
                Charaktermenu=Interaktion.Menu(SURFACE, Baer1)
                Charaktermenu.draw(SURFACE, Baer1)
                #Charaktermenu = Interaktion.Menu(SURFACE)

                #Charaktermenu.draw(SURFACE)
                #pygame.display.update()

        elif event.type==KEYDOWN:
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
    pygame.display.update()
